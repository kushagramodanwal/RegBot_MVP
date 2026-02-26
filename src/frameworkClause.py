from pydantic import BaseModel
from typing import Optional


class FrameworkClause(BaseModel):
    document_name: str
    section_number: str       
    section_title: str         
    subsection: Optional[str] 
    clause_text: str
