def get_prompt(blueprint, activities_script, warmup_script, summary_script, fact_check, dei_check, assessment_items):
    return f"""
    ## Context ##
    You are reviewing educational scripts for a social studies lesson. Each script was written for classroom instruction and intentionally excludes multimedia or instructional task references. Your job is to enhance these scripts with visual aids and interactive task suggestions that align with the lesson content.

    ## Objective ##
    Create a single support document that identifies where and how to incorporate:
    - Suggested **visuals** or multimedia elements (images, timelines, video clips, maps, animations, graphic organizers)
    - Suggested **instructional tasks** or interactive engagement moments (short writing prompts, surveys, pair-shares, timeline activities, map labeling, etc.)

    These recommendations should:
    - Enhance clarity, engagement, and student understanding
    - Align to the goals and vocabulary of the lesson
    - Be developmentally appropriate for middle and high school students
    - Address any considerations raised in the DEI and fact check reports
    - Support the assessment objectives reflected in the assessment items

    ## Response Structure ##
    Organize your response by script section:

    ### 1. Warm-Up Script
    - **Visual Suggestions:**  
      [List suggested visuals for each section of the warm-up (e.g., Anchor, Goals, Words to Know, Instruction, Check-in). Explain how each visual enhances student comprehension.]

    ### 2. Instructional Activities Script
    - **Visual Suggestions:**  
      [For each section of the instructional script, suggest relevant visual aids or multimedia elements aligned to key content and vocabulary.]

    ### 3. Summary Script
    - **Visual Suggestions:**  
      [Suggest summary visuals that would support student retention, including graphic organizers, visual timelines, or charts.]

    ### 4. Assessment Support
    - **Visual Aids for Assessment Preparation:**  
      [Suggest 2-3 key visual aids or graphic organizers that would help students prepare for the assessments.]
      
    - **Pre-Assessment Activities:**  
      [Suggest 1-2 review activities that would prepare students for success on the assessment items.]

    ## Guidelines ##
    - DO NOT rewrite or duplicate the original script content.
    - DO match suggestions to the tone and level of the original scripts.
    - DO reference vocabulary or key moments naturally without repeating full narration.
    - DO keep suggestions concise but clear enough to implement directly in a lesson build.
    - DO consider any factual or DEI issues noted in the review reports.

    ## Inputs ##
    ### Lesson Blueprint:
    {blueprint}
    
    ### Warm-Up Script:
    {warmup_script}

    ### Instructional Activity Script:
    {activities_script}

    ### Summary Script:
    {summary_script}
    
    ### Fact Check Report:
    {fact_check}
    
    ### DEI Check Report:
    {dei_check}
    
    ### Assessment Items:
    {assessment_items}
    """
