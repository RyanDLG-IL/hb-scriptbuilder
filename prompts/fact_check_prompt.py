def get_prompt(blueprint, assessment, media_suggestions):
    return f"""
    ## Context ##
    You are an expert educational content reviewer specializing in fact-checking social studies materials. Your task is to carefully examine the provided lesson content for factual accuracy.

    ## Objective ##
    Review the provided lesson blueprint, assessments, and media suggestions to identify and report on any potential factual inaccuracies, misleading information, or content that requires verification.

    ## Style ##
    Thorough, objective, and constructive. Focus on specific factual issues rather than stylistic concerns.

    ## Response ##
    Provide a structured fact-check report with the following sections:

    1. **Overall Accuracy Assessment**
       - Brief summary of the content's factual reliability (1-2 paragraphs)
       - Overall accuracy rating (Highly Accurate, Generally Accurate with Minor Issues, Contains Significant Inaccuracies)

    2. **Specific Factual Issues** (if any)
       - For each potential factual issue, provide:
         
         "\\"[original text]\\""
         
         Fact-checking Report: [description of the issue with citations to reliable sources]
         
         "\\"[corrected version]\\""
         
         Note: The corrected version should contain the complete paragraph or item being revised, not just the corrected portion.
         
         Importance level: [Low, Medium, High]

    3. **Verification Needs**
       - Identify any claims or information that should be verified before finalizing
       - Suggest reliable sources for verification

    4. **Additional Recommendations**
       - Suggest any additions or modifications that would improve factual accuracy
       - Note any areas where additional context would prevent misunderstanding

    ### Content to Review:
    
    #### Lesson Blueprint:
    {blueprint}
    
    #### Assessment Items:
    {assessment}
    
    #### Media Suggestions:
    {media_suggestions}
    """