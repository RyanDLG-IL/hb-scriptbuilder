def get_prompt(blueprint, activities_script, warmup_script, summary_script, fact_check, dei_check):
    return f"""
    ## Context
    You are an expert assessment developer for social studies education. Your task is to create assessment items that align with both the lesson blueprint AND the actual content covered in the lesson scripts. The assessment items must assess only content that appears in the lesson materials and must follow the exact structure and specifications provided below.

    ## Important Guidelines
    1. ONLY create assessment items for content that is explicitly taught in the lesson scripts (warmup, activities, and summary).
    2. Consider the recommendations from the fact check and DEI check reports when creating items.
    3. Ensure factual accuracy and cultural sensitivity in all items.
    4. Follow the DOK level guidelines strictly.
    5. Apply appropriate language and complexity for the grade level.
    6. Ensure that all generated items are multiple choice items with 4 answer choices or multiple select items with 5 answer choices.

    ### Required Assessment Items (Generate ALL of these):
    
    1. Instructional Segment 1 Item 1 (Objective 1 DOK Low) - needs Feedback
    2. Instructional Segment 1 Item 2 (Objective 1 DOK Low) - needs Feedback
    3. Instructional Segment 2 Item 1 (Objective 2 DOK Low) - needs Feedback
    4. Instructional Segment 2 Item 2 (Objective 2 DOK Low) - needs Feedback
    5. Instructional Segment 3 Item 1 (Objective 2 DOK High) - needs Feedback
    6. Instructional Segment 3 Item 2 (Objective 2 DOK High) - needs Feedback
    7. Objective 1 DOK 1 SSA Item 1 - needs Feedback
    8. Objective 1 DOK 1 SSA Item 2 - needs Feedback
    9. Objective 1 DOK 2 SSA Item 1 - needs Feedback
    10. Objective 1 DOK 2 SSA Item 2 - needs Feedback
    11. Objective 2 DOK 1 SSA Item 1 - needs Feedback
    12. Objective 2 DOK 1 SSA Item 2 - needs Feedback
    13. Objective 2 DOK 2 SSA Item 1 - needs Feedback
    14. Objective 2 DOK 2 SSA Item 2 - needs Feedback
    15. Objective 3 DOK 1 SSA Item 1 - needs Feedback
    16. Objective 3 DOK 1 SSA Item 2 - needs Feedback
    17. Objective 3 DOK 2 SSA Item 1 - needs Feedback
    18. Objective 3 DOK 2 SSA Item 2 - needs Feedback
    19. Objective 3 DOK 2 SSA Item 1 - needs Feedback
    20. Objective 3 DOK 2 SSA Item 2 - needs Feedback
    21. Objective 1 DOK 1 Assessment Item 1
    22. Objective 1 DOK 1 Assessment Item 2
    23. Objective 1 DOK 1 Assessment Item 3
    24. Objective 1 DOK 1 Assessment Item 4
    25. Objective 1 DOK 2 Assessment Item 1
    26. Objective 1 DOK 2 Assessment Item 2
    27. Objective 1 DOK 2 Assessment Item 3
    28. Objective 1 DOK 2 Assessment Item 4
    29. Objective 1 DOK 2 Assessment Item 5
    30. Objective 1 DOK 2 Assessment Item 6
    31. Objective 2 DOK 1 Assessment Item 1
    32. Objective 2 DOK 1 Assessment Item 2
    33. Objective 2 DOK 1 Assessment Item 3
    34. Objective 2 DOK 1 Assessment Item 4
    35. Objective 2 DOK 2 Assessment Item 1
    36. Objective 2 DOK 2 Assessment Item 2
    37. Objective 2 DOK 2 Assessment Item 3
    38. Objective 2 DOK 2 Assessment Item 4
    39. Objective 2 DOK 2 Assessment Item 5
    40. Objective 2 DOK 2 Assessment Item 6
    41. Objective 3 DOK 1 Assessment Item 1
    42. Objective 3 DOK 1 Assessment Item 2
    43. Objective 3 DOK 1 Assessment Item 3
    44. Objective 3 DOK 1 Assessment Item 4
    45. Objective 3 DOK 2 Assessment Item 1
    46. Objective 3 DOK 2 Assessment Item 2
    47. Objective 3 DOK 2 Assessment Item 3
    48. Objective 3 DOK 2 Assessment Item 4
    49. Objective 3 DOK 2 Assessment Item 5
    50. Objective 3 DOK 2 Assessment Item 6
    51. Objective 3 DOK 2 Assessment Item 1
    52. Objective 3 DOK 2 Assessment Item 2
    53. Objective 3 DOK 2 Assessment Item 3
    54. Objective 3 DOK 2 Assessment Item 4

    ### Social Studies DOK Level Guidelines:
    - DOK 1 (Recall of Information): Items ask students to recall facts, terms, concepts, trends, generalizations, and theories. May require students to recognize or identify specific information contained in maps, charts, tables, graphs, or other graphics. Items typically ask who, what, when, and where. Simple "describe" and "explain" tasks that require only recitation or reproduction of information are DOK 1.
    
    - DOK 2 (Basic Reasoning): Items require mental processing beyond recalling information. Students may need to compare or contrast people, places, events, and concepts; convert information from one form to another; classify items into meaningful categories; or describe/explain issues, problems, patterns, cause and effect, significance, relationships, points of view or processes in their own words. A DOK 2 explanation requires students to go beyond simple recall to discuss how or why.
   
    ### Item Format Guidelines:
    - Multiple-choice items will consist of 4 answer choices. Only 1 answer choice should be correct. 
    - Incorrect options should be based on common misconceptions or misunderstandings. 
    - Incorrect choices should seem plausible and should not be wildly incorrect. 
    - All answer choices should be parallel in style and should be roughly the same length.

    - Multiple-select items will consist of 5 answer choices. 2-3 choices should be correct. 
    - Incorrect options should be based on common misconceptions or misunderstandings. 
    - Incorrect choices should seem plausible and should not be wildly incorrect. 
    - All answer choices should be parallel in style and should be roughly the same length.

    ### Feedback Requirements:
    For items noted as needing feedback, provide targeted feedback that:
    - Anticipates misconceptions and stumbling blocks
    - Reminds students of key concepts and skills taught in the lesson
    - Supports and reinforces key learning to help students correct their answers
    - Is unique to each item and provides focused information
    - Is concise (approximately one sentence)
    - Does NOT give away the correct answer
    - Does NOT teach new concepts or approaches
    - Does NOT consist of generic boilerplate language

    ### DEI Considerations:
    - Review the DEI check report and address any issues raised
    - Ensure diverse representation in examples, scenarios, and perspectives
    - Avoid stereotypes and biases in language and content
    - Provide culturally relevant contexts when appropriate
    - Use inclusive language and examples

    ### Style Guidelines:
    - Each question item should have a Header that begins with a Gerund phrase (e.g., "Analyzing a Primary Source" or "Identifying Cause and Effect")
    - Do not use language such as "which of the following" - rather directly ask "which statement" 
    - Do not use negative questions that include "NOT," "False," or "EXCEPT" 
    - Do not use answer choices that include: "None of the above" or "all of the above"
    - US is the preferred abbreviation for the United States - not U.S.
    - Always use an Oxford comma
    - For 6th grade audience: lexile level should be 500-650
    - For 7th grade audience: lexile level should be 650-800
    - For 9th grade audience: lexile level should be 800-1000
    - For 10th grade audience: lexile level should be 900-1100

    ## Lesson Materials

    ### Lesson Blueprint:
    {blueprint}

    ### Warmup Script:
    {warmup_script}

    ### Activities Script:
    {activities_script}

    ### Summary Script:
    {summary_script}

    ## Review Reports

    ### Fact Check Report:
    {fact_check}

    ### DEI Check Report:
    {dei_check}

    Provide the assessment items in a structured format with clear sections for:
    1. Instructional Segment Items (with feedback)
    2. Self-Study Assignment Items (with feedback)
    3. Assessment Items

    For each item, include:
    - Clear item number and identification (e.g., "Instructional Segment 1 Item 1")
    - The gerund phrase header
    - The question
    - Answer choices (labeled A, B, C, D or A, B, C, D, E for multiple select)
    - Correct answer(s) clearly indicated
    - Feedback (for items that require it)
    - Clear indication of which objective and DOK level each item addresses
    
    Example format for an item with feedback:
    
    **Instructional Segment 1 Item 1 (Objective 1, DOK Level 1)**
    - Identifying Geographic Features
    
    
    Which statement correctly describes a key characteristic of Alabama's Coastal Plain region?
    
    A. It's a mountainous region with diverse flora and fauna. 
    B. It features rolling hills and fertile valleys. 
    C. It's characterized by flat, low-lying land with sandy soil and swamps. 
    D. It has high elevations and a cooler climate than other regions.
    
    Correct Answer: C
    
    Feedback: The Coastal Plain region is defined by its low elevation and flat terrain near the Gulf of Mexico.
    ----
    """