from fastapi import APIRouter
from app.schemas.chat_schema import QueryRequest, QueryResponse
from app.services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()

@router.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    answer = await rag_service.handle_query(request.query)
    return QueryResponse(answer=answer)