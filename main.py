import cohere
co = cohere.Client("Vyr79BSqb1rckbHJttVt56kV4xYm7Vvesf2Mj5Ht")

numQuestions = 1
grade = 2

prompt = f"""
Generate {numQuestions} math word problem for grade {grade}
"""

response = co.generate(
    model='xlarge',
    prompt=prompt,
    max_tokens=300,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0)

output = response.generations[0].text