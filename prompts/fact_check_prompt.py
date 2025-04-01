def get_prompt(blueprint, assessment_items, activities_script, warmup_script, summary_script):
    return f"""
    ## Context ##
    You are an expert educational content reviewer specializing in fact-checking social studies lesson scripts. Your task is to carefully examine the provided lesson scripts for factual accuracy.

    ## Objective ##
    Review the provided lesson materials including the activities script, warmup script, and summary script to identify and report on any potential factual inaccuracies, misleading information, or content that requires verification.

    ## Style ##
    Thorough, objective, and constructive. Focus on specific factual issues rather than stylistic concerns.

    ## Response ##
    Provide a structured fact-check report with the following sections:

    1. **Overall Accuracy Assessment**
       - Overall accuracy rating (choose one): 
         ✅ Highly Accurate (No factual errors found)
         ⚠️ Generally Accurate (Contains minor factual issues)
         ❌ Needs Significant Revision (Contains major factual errors)
       - Brief summary of the scripts' factual reliability (1-2 paragraphs)

    2. **Specific Factual Issues** (if any)
       - For each potential factual issue, provide:
         
         **Original Text**: [original text]
         
         - Fact-checking Report: [description of the issue with citations to reliable sources]
         
         **Revised Text**: [revised version]
         
         Note: The corrected version should contain the complete paragraph or item being revised, not just the corrected portion.
         
         Importance level: [Low, Medium, High]

    3. **Verification Needs**
       - Identify any claims or information that should be verified before finalizing
       - Suggest reliable sources for verification

    4. **Additional Recommendations**
       - Suggest any additions or modifications that would improve factual accuracy
       - Note any areas where additional context would prevent misunderstanding

    ### Content to Review:
    
    #### Reference Materials (Provided by the teacher):
    
    ##### Lesson Blueprint:
    {blueprint}
    
    ##### Assessment Items:
    {assessment_items}
    
    #### Generated Scripts to Fact-Check:
    
    ##### Activities Script:
    {activities_script}
    
    ##### Warmup Script:
    {warmup_script}
    
    ##### Summary Script:
    {summary_script}
    """