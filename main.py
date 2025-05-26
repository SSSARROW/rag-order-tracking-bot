from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
from order_tracking import get_order_status
import re

model = OllamaLLM(model="gemma3:4b")

template = """
You are a helpful AI assistant for an eCommerce website. Your main job is to help customers track their orders and answer questions about order status, delivery times, shipment details, as well as general questions about products, returns, payments, and policies.

Only use the provided context (answers) below to answer.

If the question is about a specific order and you have order information, provide details.

If the question is about an order but no order ID or info is provided, politely ask the user to provide their order ID.

If the question is unrelated to orders, answer based on the context.
Here are Some relevant Answers:{answers}
Please answer the question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



def extract_order_id(question):
    match = re.search(r'\b\d{5,}\b', question)  # finds number with 5+ digits
    return match.group(0) if match else None


    
    
while True:
    question = input("Enter your question (q to quit): ")
    if question.lower() == "q":
        break

    order_id = extract_order_id(question)
    if order_id:
        # We have an order ID, so fetch live order info
        live_answer = get_order_status(order_id)
        # Combine live answer with context from vector DB
        answers = retriever.invoke(question)
        full_context = "\n".join([doc.page_content for doc in answers]) + "\n" + live_answer

        result = chain.invoke({"question": question, "answers": full_context})
        print(result)
    else:
        # No order ID found, just answer from vector DB
        answers = retriever.invoke(question)
        result = chain.invoke({"question": question, "answers": answers})
        print(result)
