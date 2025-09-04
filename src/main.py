from fastapi import FastAPI, UploadFile, File, HTTPException
from src.database.client import prisma
from src.processing.document_handler import process_document

app = FastAPI(title="Document Processing API")

@app.post("/process-document/")
async def process_document_endpoint(file: UploadFile = File(...)):
    """
    Process an uploaded document and store the extracted text in the database.

    Args:
        file (UploadFile): The uploaded file.

    Returns:
        dict: A JSON response with the ID of the created database record.
    """
    try:
        # Connect to database (serverless-friendly)
        await prisma.connect()

        # Read file content
        file_bytes = await file.read()

        # Process the document
        transcripted_content = process_document(file.filename, file_bytes)

        # Save to database
        processed_doc = await prisma.processeddocument.create(
            data={
                "sourceFileName": file.filename,
                "transcriptedContent": transcripted_content,
            }
        )

        # Disconnect from database
        await prisma.disconnect()

        return {"id": processed_doc.id}

    except ValueError as e:
        await prisma.disconnect()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await prisma.disconnect()
        raise HTTPException(status_code=500, detail="Internal server error")
