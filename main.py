def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()


print("Rimsha")
print("Princess")
print("I am in the class")
from fastapi import FastAPI
app = FastAPI(title="Client Negotiation Practice Agent")

@app.get("/")
def read_root():
    return {"message": "Hello from backend!"}

@app.get("/health")
def read_health():
    return {"status": "ok"}