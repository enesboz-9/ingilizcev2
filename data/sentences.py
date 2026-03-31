# Sentence patterns organized by grammar category

SENTENCE_PATTERNS = {
    "📌 Be Verb (To Be)": [
        {
            "pattern": "Subject + am/is/are + Noun/Adjective",
            "formula": "I am + adj | He/She/It is + noun | We/You/They are + adj",
            "level": "A1",
            "examples": [
                "I am a student.",
                "She is beautiful.",
                "They are from Turkey.",
            ],
            "note": "Use 'am' with I, 'is' with he/she/it, 'are' with you/we/they.",
        },
        {
            "pattern": "Subject + was/were + Noun/Adjective",
            "formula": "I/He/She/It was + adj | We/You/They were + noun",
            "level": "A1",
            "examples": [
                "I was tired yesterday.",
                "The party was great.",
                "They were late.",
            ],
            "note": "Past tense of 'to be'. 'Was' for singular, 'were' for plural.",
        },
    ],
    "📌 Present Simple": [
        {
            "pattern": "Subject + base verb (+ s/es for he/she/it)",
            "formula": "I/You/We/They + V | He/She/It + V+s",
            "level": "A1",
            "examples": [
                "I drink coffee every morning.",
                "She works at a bank.",
                "They play football on weekends.",
            ],
            "note": "Used for habits, facts, and regular actions.",
        },
        {
            "pattern": "Subject + do/does + not + base verb",
            "formula": "I don't + V | She doesn't + V",
            "level": "A1",
            "examples": [
                "I don't eat meat.",
                "He doesn't like cold weather.",
                "They don't speak French.",
            ],
            "note": "Negative form: use 'don't' / 'doesn't' + base verb.",
        },
        {
            "pattern": "Do/Does + Subject + base verb?",
            "formula": "Do + I/you/we/they + V? | Does + he/she/it + V?",
            "level": "A1",
            "examples": [
                "Do you like pizza?",
                "Does she speak English?",
                "Do they live here?",
            ],
            "note": "Question form. Answer: Yes, I do. / No, she doesn't.",
        },
    ],
    "📌 Present Continuous": [
        {
            "pattern": "Subject + am/is/are + verb-ing",
            "formula": "I am + V-ing | He is + V-ing | They are + V-ing",
            "level": "A2",
            "examples": [
                "I am studying English right now.",
                "She is cooking dinner.",
                "They are watching TV.",
            ],
            "note": "Used for actions happening at the moment of speaking.",
        },
        {
            "pattern": "Subject + am/is/are + verb-ing (future plan)",
            "formula": "I am + V-ing + time expression",
            "level": "A2",
            "examples": [
                "We are meeting tomorrow.",
                "She is flying to London next week.",
                "I am starting a new job on Monday.",
            ],
            "note": "Also used for definite future plans.",
        },
    ],
    "📌 Past Simple": [
        {
            "pattern": "Subject + verb-ed (regular) / V2 (irregular)",
            "formula": "I/He/She/They + V-ed | went, saw, bought...",
            "level": "A2",
            "examples": [
                "I visited Paris last year.",
                "She went to the market.",
                "They bought a new car.",
            ],
            "note": "Used for completed actions in the past. Learn irregular verbs!",
        },
        {
            "pattern": "Subject + did not + base verb",
            "formula": "I didn't + V (base form)",
            "level": "A2",
            "examples": [
                "I didn't sleep well last night.",
                "She didn't come to the party.",
                "They didn't finish the project.",
            ],
            "note": "Negative past: always use 'didn't' + base verb (not V2).",
        },
    ],
    "📌 Future Tenses": [
        {
            "pattern": "Subject + will + base verb",
            "formula": "I will + V (base)",
            "level": "A2",
            "examples": [
                "I will call you later.",
                "She will help you.",
                "It will be cold tomorrow.",
            ],
            "note": "Used for decisions made at the moment, predictions, promises.",
        },
        {
            "pattern": "Subject + am/is/are going to + base verb",
            "formula": "I am going to + V | She is going to + V",
            "level": "A2",
            "examples": [
                "I am going to study tonight.",
                "They are going to move next month.",
                "Look at those clouds — it is going to rain.",
            ],
            "note": "Used for plans and intentions, or predictions based on evidence.",
        },
    ],
    "📌 Present Perfect": [
        {
            "pattern": "Subject + have/has + past participle",
            "formula": "I/You/We/They have + V3 | He/She/It has + V3",
            "level": "B1",
            "examples": [
                "I have visited London three times.",
                "She has already eaten.",
                "They have just arrived.",
            ],
            "note": "Use for: experiences, recent actions (just/already), unfinished states.",
        },
        {
            "pattern": "Subject + have/has + been + verb-ing",
            "formula": "I have been + V-ing (for/since)",
            "level": "B1",
            "examples": [
                "I have been learning English for two years.",
                "She has been working here since 2020.",
                "They have been waiting for an hour.",
            ],
            "note": "Present Perfect Continuous — emphasises duration of an ongoing activity.",
        },
    ],
    "📌 Modal Verbs": [
        {
            "pattern": "Subject + can/could + base verb",
            "formula": "I can + V | I could + V",
            "level": "A2",
            "examples": [
                "I can swim very well.",
                "Could you help me please?",
                "She could speak three languages at 12.",
            ],
            "note": "'Can' = ability/permission. 'Could' = past ability or polite request.",
        },
        {
            "pattern": "Subject + must/have to + base verb",
            "formula": "I must + V | I have to + V",
            "level": "B1",
            "examples": [
                "You must wear a seatbelt.",
                "I have to finish this by Friday.",
                "She has to take medicine twice a day.",
            ],
            "note": "'Must' = strong obligation (speaker). 'Have to' = external obligation.",
        },
        {
            "pattern": "Subject + should + base verb",
            "formula": "I should + V | You should + V",
            "level": "A2",
            "examples": [
                "You should drink more water.",
                "She should apologise.",
                "We shouldn't waste food.",
            ],
            "note": "Used for advice and recommendations.",
        },
        {
            "pattern": "Subject + might/may + base verb",
            "formula": "I might + V (possibility)",
            "level": "B1",
            "examples": [
                "It might rain tomorrow.",
                "She may be late.",
                "I might visit Istanbul next summer.",
            ],
            "note": "'May' and 'might' both express possibility. 'Might' is slightly less certain.",
        },
    ],
    "📌 Conditional Sentences": [
        {
            "pattern": "If + Present Simple, will + base verb (Zero/First Conditional)",
            "formula": "If + S + V, S + will + V",
            "level": "B1",
            "examples": [
                "If you study hard, you will pass.",
                "If it rains, we will stay inside.",
                "If she calls, I will answer.",
            ],
            "note": "Real or possible situations in the present or future.",
        },
        {
            "pattern": "If + Past Simple, would + base verb (Second Conditional)",
            "formula": "If + S + V-ed, S + would + V",
            "level": "B2",
            "examples": [
                "If I had a million dollars, I would travel the world.",
                "If she knew the answer, she would tell us.",
                "If I were you, I would apologise.",
            ],
            "note": "Imaginary or hypothetical situations. Note: use 'were' not 'was' with 'I' in formal English.",
        },
        {
            "pattern": "If + Past Perfect, would have + past participle (Third Conditional)",
            "formula": "If + S + had + V3, S + would have + V3",
            "level": "C1",
            "examples": [
                "If I had studied more, I would have passed.",
                "If she had arrived earlier, she would have caught the train.",
                "If they had known, they would have helped.",
            ],
            "note": "Imagining a different past. Always refers to something that did NOT happen.",
        },
    ],
    "📌 Passive Voice": [
        {
            "pattern": "Subject + am/is/are + past participle (by agent)",
            "formula": "S + is/are + V3 (+ by + agent)",
            "level": "B1",
            "examples": [
                "English is spoken worldwide.",
                "This building was designed by a famous architect.",
                "The report will be submitted tomorrow.",
            ],
            "note": "Use passive when the action is more important than who does it.",
        },
    ],
    "📌 Reported Speech": [
        {
            "pattern": "Subject + said (that) + clause (backshift)",
            "formula": "She said (that) + S + V (shifted back)",
            "level": "B2",
            "examples": [
                "She said that she was tired.",
                "He told me he had finished the work.",
                "They said they would come later.",
            ],
            "note": "Tenses shift back when reporting: present → past, will → would, can → could.",
        },
    ],
    "📌 Relative Clauses": [
        {
            "pattern": "Noun + who/which/that + clause",
            "formula": "The person who + V | The book which + V",
            "level": "B1",
            "examples": [
                "The woman who called you is my sister.",
                "This is the book that changed my life.",
                "The house which we visited was amazing.",
            ],
            "note": "'Who' for people, 'which' for things, 'that' for both (defining clauses).",
        },
    ],
    "📌 Causative (Have/Get)": [
        {
            "pattern": "Subject + have/get + object + past participle",
            "formula": "I had/got + object + V3",
            "level": "C1",
            "examples": [
                "I had my hair cut yesterday.",
                "She got her car repaired.",
                "We had the house painted.",
            ],
            "note": "Used when you arrange for someone else to do something for you.",
        },
    ],
    "📌 Inversion (Advanced)": [
        {
            "pattern": "Negative adverbial + auxiliary + subject + verb",
            "formula": "Never/Rarely/Hardly + aux + S + V",
            "level": "C2",
            "examples": [
                "Never have I seen such courage.",
                "Rarely does she complain.",
                "Not only did he win, but he also broke the record.",
            ],
            "note": "Used for emphasis in formal/literary English. Puts auxiliary before subject.",
        },
    ],
}
