import cohere

def generate_math_problems(grade_level):
    co = cohere.Client("Vyr79BSqb1rckbHJttVt56kV4xYm7Vvesf2Mj5Ht")
    prompt = f"Generate some math problems for grade {grade_level}"
    response = co.generate(
        model='xlarge',
        prompt = prompt,
        max_tokens=80,
        temperature=0.0,
        stop_sequences=["--"])
    answer = response.generations[0].text
    print(answer)

generate_math_problems(2)
