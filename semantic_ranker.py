from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_resumes(job_description, resumes):

    documents = [job_description] + resumes

    embeddings = model.encode(documents)

    job_embedding = embeddings[0]
    resume_embeddings = embeddings[1:]

    scores = cosine_similarity(
        [job_embedding], resume_embeddings
    )[0]

    return scores