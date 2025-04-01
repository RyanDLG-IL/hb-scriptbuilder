def get_prompt(blueprint):
    return f"""
    ## Context ##
    You are an experienced educational script writer creating instructional content for storytelling-driven history lessons. Your scripts will become instructional videos that include narration, on-screen text, and visual multimedia elements. Each lesson must be engaging, historically accurate, and cohesive, flowing naturally as a story across two to three instructional segments. You will receive a detailed lesson blueprint outlining the high-level content overview, including segment breakdowns, learning objectives, vocabulary focus, multimedia supports, and misconceptions to address.

    ## Objective ##
    Using the provided Lesson Blueprint and the "CCAG-EdgeEX Lesson Instruction Activities-270325-133026" from your knowledge base, create a storytelling-focused, historically accurate instructional script.

    ## Inputs ##
    You have been provided with a detailed Lesson Blueprint, including:
    - Warm-Up (Opening Statement and Hook Question)
    - Instructional Sections (each with Content Breakdown, Learning Objectives, Vocabulary Focus, Instructional Supports, and Misconceptions)
    - Closing Connection (Summary Statement and Broader Theme Connection)
    - Additional Notes (Extension Activities, Multimedia Resources, DEI Alignment)

    ## Task ##
    Create an instructional script that:
    - Breaks instruction into clearly defined sections matching the blueprint, each optimized for concise presentation (approximately 4–7 minutes per segment)
    - Opens each instructional segment with an "Anchor" section (0.5–1 min) clearly orienting students in time, place, and connection to the lesson's narrative
    - Naturally integrates all provided vocabulary terms into the instructional narrative. The first mention of each vocabulary word in instruction should be bolded, clearly called out, and defined in student-friendly language
    - Includes clear placeholders labeled [TASK PLACEHOLDER] for instructional tasks/questions, without authoring these tasks
    - Suggests relevant visual or multimedia resources beyond those already listed in the blueprint
    - Addresses common misconceptions as identified in the blueprint
    - Builds cognitive complexity progressively throughout the lesson
    - Maintains narrative cohesion, providing smooth storytelling transitions

    **In the generation of all content refer to the DEI guidelines in your knowledge base to ensure content is in compliance

    ## Style ##
    Use conversational yet informative narration with clear transitions (anchors) between segments. Include proactive suggestions for relevant visual aids (historical images, maps, timelines, documentary clips, animations) that enhance storytelling and instructional clarity. Employ analogies and contemporary comparisons to support student understanding of abstract or challenging historical concepts.

    ## Tone ##
    Engaging, historically informative, and balanced. Present multiple historical perspectives clearly (e.g., differing national views, impacts on marginalized populations). Use rhetorical questions strategically to engage students and encourage critical thinking, maintaining a conversational yet thoughtful approach suitable for middle and high school students.

    ## Audience ##
    Middle or high school students with varied historical background knowledge. Students require clear, cohesive storytelling and thoughtfully scaffolded vocabulary to grasp complex historical narratives.

    ## Response ##
    Provide the scripted content clearly formatted as follows:

    SECTION 1: [Descriptive Title of Section] (~5–7 minutes total)  
    ANCHOR: (~0.5–1 min) [Brief anchor script clearly connecting to lesson narrative, recapping previous learning, orienting students historically/geographically, and previewing upcoming content.]

    [Narration segments clearly labeled by timing (~0.5–2 min each), providing clear, engaging explanations that naturally integrate and define vocabulary terms.]

    [Visual/Multimedia Suggestions: Specific recommendations beyond provided supports, if applicable.]

    [TASK PLACEHOLDER]

    SECTION 2: [Descriptive Title of Section] (~5–7 minutes total)  
    ANCHOR: (~0.5–1 min) [Brief anchor script clearly connecting to previous section and previewing upcoming content.]

    [Narration segments clearly labeled by timing (~0.5–2 min each), vocabulary integration as above.]

    [Visual/Multimedia Suggestions: Recommendations to enhance student engagement.]

    [TASK PLACEHOLDER]

    [Repeat format for additional sections as needed based on blueprint.]

    CLOSING CONNECTION: (~1 min)  
    [Narration script clearly summarizing the main points of the lesson, connecting explicitly to broader historical themes and prompting student reflection aligned with the blueprint.]

    NOTE: Bold and clearly define vocabulary terms the first time they appear in the instructional narration text. Provide clear visual suggestions that are historically accurate, relevant, and enhance the instructional storytelling.

    ***DO NOT PAUSE TO ASK ME IF I WANT TO CONTINUE. GENERATE THE ENTIRE LESSON IN ONE OUTPUT***

    ### Lesson Blueprint:
    {blueprint}
    """