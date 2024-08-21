from prompt import prompt_text
from file_loader import get_content
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = prompt_text

print(template)

contract_loc = "docs/Contracts/20230317_The_City_of_Seattle_Original_Contract_Award.pdf"
invoice_loc ="docs/Invoices/424216.pdf"

contract_content = get_content(contract_loc)

invoice_content = get_content(invoice_loc)

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:latest")

chain = prompt | model

response = chain.invoke({"CONTRACT_TEXT": contract_content,
                         "INVOICE_TEXT": invoice_content})
print(response)