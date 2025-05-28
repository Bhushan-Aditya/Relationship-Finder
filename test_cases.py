test_cases = [
    {
        "text": "Vihaan is Xara's mother. Xara is Kiara's daughter.",
        "question": "how is Vihaan related to Kiara",
        "expected": "Vihaan is Kiara's grandmother"
    },
    {
        "text": "Ovi is Kiara's husband. Kiara is Naina's mother.",
        "question": "how is Ovi related to Naina",
        "expected": "Ovi is Naina's father-in-law"
    },
    {
        "text": "Ishaan is Ojas's sister. Ojas is Sara's daughter.",
        "question": "how is Ishaan related to Sara",
        "expected": "Ishaan is Sara's aunt"
    },
    {
        "text": "Ojas is Harsh's sister. Harsh is Pari's daughter.",
        "question": "how is Ojas related to Pari",
        "expected": "Ojas is Pari's aunt"
    },
    {
        "text": "Ovi is Xara's son. Xara is Uma's daughter.",
        "question": "how is Ovi related to Uma",
        "expected": "Ovi is Uma's brother"
    },
    {
        "text": "Yash is Aanya's husband. Aanya is Diya's mother.",
        "question": "how is Yash related to Diya",
        "expected": "Yash is Diya's father-in-law"
    },
    {
        "text": "Dev is Anaya's father. Anaya is Aditya's son.",
        "question": "how is Dev related to Aditya",
        "expected": "Dev is Aditya's grandfather"
    },
    {
        "text": "Kiara is Farhan's mother. Farhan is Uma's daughter.",
        "question": "how is Kiara related to Uma",
        "expected": "Kiara is Uma's grandmother"
    },
    {
        "text": "Diya is Mira's brother. Mira is Anaya's brother.",
        "question": "how is Diya related to Anaya",
        "expected": "Diya is Anaya's brother"
    },
    {
        "text": "Kavya is Vivaan's father. Vivaan is Diya's son.",
        "question": "how is Kavya related to Diya",
        "expected": "Kavya is Diya's grandfather"
    },
    {
        "text": "Ira is Myra's wife. Myra is Aditya's father.",
        "question": "how is Ira related to Aditya",
        "expected": "Ira is Aditya's mother-in-law"
    },
    {
        "text": "Bhavya is Laksh's father. Laksh is Naina's son.",
        "question": "how is Bhavya related to Naina",
        "expected": "Bhavya is Naina's grandfather"
    },
    {
        "text": "Ojas is Dev's cousin. Dev is Aadhya's cousin.",
        "question": "how is Ojas related to Aadhya",
        "expected": "Ojas is Aadhya's cousin"
    },
    {
        "text": "Aditya is Zara's sister. Zara is Dev's daughter.",
        "question": "how is Aditya related to Dev",
        "expected": "Aditya is Dev's aunt"
    },
    {
        "text": "Mira is Jay's sister. Jay is Uma's sister.",
        "question": "how is Mira related to Uma",
        "expected": "Mira is Uma's sister"
    },
    {
        "text": "Aarav is Myra's sister. Myra is Bhavya's sister.",
        "question": "how is Aarav related to Bhavya",
        "expected": "Aarav is Bhavya's sister"
    },
    {
        "text": "Aarav is Pari's wife. Pari is Vihaan's father.",
        "question": "how is Aarav related to Vihaan",
        "expected": "Aarav is Vihaan's mother-in-law"
    },
    {
        "text": "Eva is Ishaan's sister. Ishaan is Bhavya's son.",
        "question": "how is Eva related to Bhavya",
        "expected": "Eva is Bhavya's aunt"
    },
    {
        "text": "Aditya is Saanvi's sister. Saanvi is Zara's son.",
        "question": "how is Aditya related to Zara",
        "expected": "Aditya is Zara's aunt"
    },
    {
        "text": "Reyansh is Aanya's sister. Aanya is Neel's sister.",
        "question": "how is Reyansh related to Neel",
        "expected": "Reyansh is Neel's sister"
    },
    {
        "text": "Yash is Rohan's brother. Rohan is Aditya's daughter.",
        "question": "how is Yash related to Aditya",
        "expected": "Yash is Aditya's uncle"
    },
    {
        "text": "Reyansh is Eva's sister. Eva is Ovi's daughter.",
        "question": "how is Reyansh related to Ovi",
        "expected": "Reyansh is Ovi's aunt"
    },
    {
        "text": "Dev is Aarav's mother. Aarav is Kiara's son.",
        "question": "how is Dev related to Kiara",
        "expected": "Dev is Kiara's grandmother"
    },
    {
        "text": "Kiara is Anaya's mother. Anaya is Vivaan's daughter.",
        "question": "how is Kiara related to Vivaan",
        "expected": "Kiara is Vivaan's grandmother"
    },
    {
        "text": "Wafa is Gia's son. Gia is Aryan's daughter.",
        "question": "how is Wafa related to Aryan",
        "expected": "Wafa is Aryan's brother"
    },
    {
        "text": "Anaya is Wafa's brother. Wafa is Tara's brother.",
        "question": "how is Anaya related to Tara",
        "expected": "Anaya is Tara's brother"
    },
    {
        "text": "Jay is Uma's brother. Uma is Harsh's daughter.",
        "question": "how is Jay related to Harsh",
        "expected": "Jay is Harsh's uncle"
    },
    {
        "text": "Myra is Jay's father. Jay is Ved's daughter.",
        "question": "how is Myra related to Ved",
        "expected": "Myra is Ved's grandfather"
    },
    {
        "text": "Ojas is Ishaan's brother. Ishaan is Zara's son.",
        "question": "how is Ojas related to Zara",
        "expected": "Ojas is Zara's uncle"
    },
    {
        "text": "Eva is Aryan's son. Aryan is Diya's daughter.",
        "question": "how is Eva related to Diya",
        "expected": "Eva is Diya's brother"
    },
    {
        "text": "Kavya is Ovi's mother. Ovi is Vivaan's daughter.",
        "question": "how is Kavya related to Vivaan",
        "expected": "Kavya is Vivaan's grandmother"
    },
    {
        "text": "Dev is Wafa's son. Wafa is Ojas's daughter.",
        "question": "how is Dev related to Ojas",
        "expected": "Dev is Ojas's brother"
    },
    {
        "text": "Ovi is Xara's sister. Xara is Aditya's son.",
        "question": "how is Ovi related to Aditya",
        "expected": "Ovi is Aditya's aunt"
    },
    {
        "text": "Zara is Aanya's mother. Aanya is Reyansh's daughter.",
        "question": "how is Zara related to Reyansh",
        "expected": "Zara is Reyansh's grandmother"
    },
    {
        "text": "Eva is Reyansh's sister. Reyansh is Aditya's sister.",
        "question": "how is Eva related to Aditya",
        "expected": "Eva is Aditya's sister"
    },
    {
        "text": "Aadhya is Eva's mother. Eva is Aarav's daughter.",
        "question": "how is Aadhya related to Aarav",
        "expected": "Aadhya is Aarav's grandmother"
    },
    {
        "text": "Xara is Wafa's sister. Wafa is Pari's sister.",
        "question": "how is Xara related to Pari",
        "expected": "Xara is Pari's sister"
    },
    {
        "text": "Vihaan is Yash's wife. Yash is Bhavya's father.",
        "question": "how is Vihaan related to Bhavya",
        "expected": "Vihaan is Bhavya's mother-in-law"
    },
    {
        "text": "Mira is Rohan's cousin. Rohan is Ojas's cousin.",
        "question": "how is Mira related to Ojas",
        "expected": "Mira is Ojas's cousin"
    },
    {
        "text": "Jay is Xara's father. Xara is Mira's son.",
        "question": "how is Jay related to Mira",
        "expected": "Jay is Mira's grandfather"
    },
    {
        "text": "Ojas is Naina's brother. Naina is Kiara's daughter.",
        "question": "how is Ojas related to Kiara",
        "expected": "Ojas is Kiara's uncle"
    },
    {
        "text": "Vivaan is Uma's father. Uma is Bhavya's son.",
        "question": "how is Vivaan related to Bhavya",
        "expected": "Vivaan is Bhavya's grandfather"
    },
    {
        "text": "Dev is Gia's sister. Gia is Bhavya's sister.",
        "question": "how is Dev related to Bhavya",
        "expected": "Dev is Bhavya's sister"
    },
    {
        "text": "Aditya is Naina's daughter. Naina is Myra's son.",
        "question": "how is Aditya related to Myra",
        "expected": "Aditya is Myra's sister"
    },
    {
        "text": "Zara is Tara's mother. Tara is Aditya's son.",
        "question": "how is Zara related to Aditya",
        "expected": "Zara is Aditya's grandmother"
    },
    {
        "text": "Naina is Xara's son. Xara is Ovi's daughter.",
        "question": "how is Naina related to Ovi",
        "expected": "Naina is Ovi's brother"
    },
    {
        "text": "Ovi is Ved's cousin. Ved is Kavya's cousin.",
        "question": "how is Ovi related to Kavya",
        "expected": "Ovi is Kavya's cousin"
    },
    {
        "text": "Ovi is Ira's husband. Ira is Ojas's mother.",
        "question": "how is Ovi related to Ojas",
        "expected": "Ovi is Ojas's father-in-law"
    },
    {
        "text": "Tara is Diya's wife. Diya is Vivaan's father.",
        "question": "how is Tara related to Vivaan",
        "expected": "Tara is Vivaan's mother-in-law"
    },
    {
        "text": "Bhavya is Sara's brother. Sara is Kavya's brother.",
        "question": "how is Bhavya related to Kavya",
        "expected": "Bhavya is Kavya's brother"
    },
    {
        "text": "Farhan is Myra's brother. Myra is Aarav's daughter.",
        "question": "how is Farhan related to Aarav",
        "expected": "Farhan is Aarav's uncle"
    },
    {
        "text": "Aditya is Gia's mother. Gia is Ojas's daughter.",
        "question": "how is Aditya related to Ojas",
        "expected": "Aditya is Ojas's grandmother"
    },
    {
        "text": "Aarav is Xara's brother. Xara is Wafa's daughter.",
        "question": "how is Aarav related to Wafa",
        "expected": "Aarav is Wafa's uncle"
    },
    {
        "text": "Laksh is Bhavya's husband. Bhavya is Yash's mother.",
        "question": "how is Laksh related to Yash",
        "expected": "Laksh is Yash's father-in-law"
    },
    {
        "text": "Jay is Aanya's daughter. Aanya is Mira's son.",
        "question": "how is Jay related to Mira",
        "expected": "Jay is Mira's sister"
    },
    {
        "text": "Eva is Rohan's sister. Rohan is Neel's daughter.",
        "question": "how is Eva related to Neel",
        "expected": "Eva is Neel's aunt"
    },
    {
        "text": "Aanya is Laksh's husband. Laksh is Kiara's mother.",
        "question": "how is Aanya related to Kiara",
        "expected": "Aanya is Kiara's father-in-law"
    },
    {
        "text": "Ishaan is Saanvi's father. Saanvi is Xara's daughter.",
        "question": "how is Ishaan related to Xara",
        "expected": "Ishaan is Xara's grandfather"
    },
    {
        "text": "Pari is Saanvi's father. Saanvi is Aryan's daughter.",
        "question": "how is Pari related to Aryan",
        "expected": "Pari is Aryan's grandfather"
    },
    {
        "text": "Uma is Aditya's father. Aditya is Saanvi's son.",
        "question": "how is Uma related to Saanvi",
        "expected": "Uma is Saanvi's grandfather"
    },
    {
        "text": "Aadhya is Vihaan's cousin. Vihaan is Xara's cousin.",
        "question": "how is Aadhya related to Xara",
        "expected": "Aadhya is Xara's cousin"
    },
    {
        "text": "Ishaan is Anaya's brother. Anaya is Ojas's brother.",
        "question": "how is Ishaan related to Ojas",
        "expected": "Ishaan is Ojas's brother"
    },
    {
        "text": "Vivaan is Diya's sister. Diya is Saanvi's daughter.",
        "question": "how is Vivaan related to Saanvi",
        "expected": "Vivaan is Saanvi's aunt"
    },
    {
        "text": "Dev is Sara's mother. Sara is Ovi's daughter.",
        "question": "how is Dev related to Ovi",
        "expected": "Dev is Ovi's grandmother"
    },
    {
        "text": "Jay is Tara's husband. Tara is Vihaan's mother.",
        "question": "how is Jay related to Vihaan",
        "expected": "Jay is Vihaan's father-in-law"
    },
    {
        "text": "Anaya is Yash's brother. Yash is Kiara's brother.",
        "question": "how is Anaya related to Kiara",
        "expected": "Anaya is Kiara's brother"
    },
    {
        "text": "Reyansh is Ovi's mother. Ovi is Saanvi's son.",
        "question": "how is Reyansh related to Saanvi",
        "expected": "Reyansh is Saanvi's grandmother"
    },
    {
        "text": "Eva is Myra's mother. Myra is Bhavya's son.",
        "question": "how is Eva related to Bhavya",
        "expected": "Eva is Bhavya's grandmother"
    },
    {
        "text": "Ira is Aryan's brother. Aryan is Diya's brother.",
        "question": "how is Ira related to Diya",
        "expected": "Ira is Diya's brother"
    },
    {
        "text": "Aanya is Yash's sister. Yash is Pari's sister.",
        "question": "how is Aanya related to Pari",
        "expected": "Aanya is Pari's sister"
    },
    {
        "text": "Aanya is Sara's mother. Sara is Naina's son.",
        "question": "how is Aanya related to Naina",
        "expected": "Aanya is Naina's grandmother"
    },
    {
        "text": "Harsh is Kiara's mother. Kiara is Aanya's daughter.",
        "question": "how is Harsh related to Aanya",
        "expected": "Harsh is Aanya's grandmother"
    },
    {
        "text": "Farhan is Reyansh's mother. Reyansh is Harsh's daughter.",
        "question": "how is Farhan related to Harsh",
        "expected": "Farhan is Harsh's grandmother"
    },
    {
        "text": "Dev is Xara's brother. Xara is Naina's daughter.",
        "question": "how is Dev related to Naina",
        "expected": "Dev is Naina's uncle"
    },
    {
        "text": "Yash is Eva's mother. Eva is Ovi's son.",
        "question": "how is Yash related to Ovi",
        "expected": "Yash is Ovi's grandmother"
    },
    {
        "text": "Laksh is Wafa's brother. Wafa is Zara's son.",
        "question": "how is Laksh related to Zara",
        "expected": "Laksh is Zara's uncle"
    },
    {
        "text": "Eva is Myra's brother. Myra is Bhavya's daughter.",
        "question": "how is Eva related to Bhavya",
        "expected": "Eva is Bhavya's uncle"
    },
    {
        "text": "Zara is Kavya's sister. Kavya is Laksh's sister.",
        "question": "how is Zara related to Laksh",
        "expected": "Zara is Laksh's sister"
    },
    {
        "text": "Kiara is Ishaan's brother. Ishaan is Harsh's son.",
        "question": "how is Kiara related to Harsh",
        "expected": "Kiara is Harsh's uncle"
    },
    {
        "text": "Harsh is Saanvi's daughter. Saanvi is Tara's son.",
        "question": "how is Harsh related to Tara",
        "expected": "Harsh is Tara's sister"
    },
    {
        "text": "Neel is Vihaan's wife. Vihaan is Bhavya's father.",
        "question": "how is Neel related to Bhavya",
        "expected": "Neel is Bhavya's mother-in-law"
    },
    {
        "text": "Vihaan is Rohan's brother. Rohan is Ishaan's daughter.",
        "question": "how is Vihaan related to Ishaan",
        "expected": "Vihaan is Ishaan's uncle"
    },
    {
        "text": "Vivaan is Zara's husband. Zara is Ojas's mother.",
        "question": "how is Vivaan related to Ojas",
        "expected": "Vivaan is Ojas's father-in-law"
    },
    {
        "text": "Aadhya is Tara's mother. Tara is Yash's daughter.",
        "question": "how is Aadhya related to Yash",
        "expected": "Aadhya is Yash's grandmother"
    },
    {
        "text": "Tara is Aanya's husband. Aanya is Ojas's mother.",
        "question": "how is Tara related to Ojas",
        "expected": "Tara is Ojas's father-in-law"
    },
    {
        "text": "Aadhya is Tara's sister. Tara is Rohan's son.",
        "question": "how is Aadhya related to Rohan",
        "expected": "Aadhya is Rohan's aunt"
    },
    {
        "text": "Eva is Diya's son. Diya is Aanya's daughter.",
        "question": "how is Eva related to Aanya",
        "expected": "Eva is Aanya's brother"
    },
    {
        "text": "Diya is Ishaan's daughter. Ishaan is Sara's son.",
        "question": "how is Diya related to Sara",
        "expected": "Diya is Sara's sister"
    },
    {
        "text": "Reyansh is Kiara's daughter. Kiara is Ishaan's son.",
        "question": "how is Reyansh related to Ishaan",
        "expected": "Reyansh is Ishaan's sister"
    },
    {
        "text": "Pari is Vivaan's wife. Vivaan is Kabir's father.",
        "question": "how is Pari related to Kabir",
        "expected": "Pari is Kabir's mother-in-law"
    },
    {
        "text": "Eva is Diya's mother. Diya is Mira's son.",
        "question": "how is Eva related to Mira",
        "expected": "Eva is Mira's grandmother"
    },
    {
        "text": "Aarav is Eva's mother. Eva is Vivaan's daughter.",
        "question": "how is Aarav related to Vivaan",
        "expected": "Aarav is Vivaan's grandmother"
    },
    {
        "text": "Eva is Jay's father. Jay is Ira's son.",
        "question": "how is Eva related to Ira",
        "expected": "Eva is Ira's grandfather"
    },
    {
        "text": "Uma is Farhan's father. Farhan is Ovi's daughter.",
        "question": "how is Uma related to Ovi",
        "expected": "Uma is Ovi's grandfather"
    },
    {
        "text": "Dev is Kiara's son. Kiara is Ishaan's daughter.",
        "question": "how is Dev related to Ishaan",
        "expected": "Dev is Ishaan's brother"
    },
    {
        "text": "Dev is Kabir's mother. Kabir is Aditya's son.",
        "question": "how is Dev related to Aditya",
        "expected": "Dev is Aditya's grandmother"
    },
    {
        "text": "Bhavya is Ira's sister. Ira is Tara's son.",
        "question": "how is Bhavya related to Tara",
        "expected": "Bhavya is Tara's aunt"
    },
    {
        "text": "Gia is Eva's brother. Eva is Aadhya's son.",
        "question": "how is Gia related to Aadhya",
        "expected": "Gia is Aadhya's uncle"
    },
    {
        "text": "Diya is Ved's daughter. Ved is Gia's son.",
        "question": "how is Diya related to Gia",
        "expected": "Diya is Gia's sister"
    },
    {
        "text": "Ojas is Aryan's daughter. Aryan is Aarav's son.",
        "question": "how is Ojas related to Aarav",
        "expected": "Ojas is Aarav's sister"
    }
]