import os
import google.generativeai as genai

# Initialize Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def please_help_me_solve(error_msg, provide_code=False):
    try:
        # Get the current file's content if provide_code is True
        code_context = ""
        if provide_code:
            try:
                with open(__file__, 'r') as file:
                    code_context = f"\nCODE CONTEXT:\n{file.read()}"
            except:
                code_context = "\nCould not read the source code."
        
        prompt = f'''YOU ARE A HELPFUL CODE ASSISTANT WHICH HELPS CODERS TO FIX BUGS
        YOU ARE GIVEN AN ERROR MESSAGE. DETECT THE PROBLEM THAT IS OCCURING IN THAT ERROR MESSAGE. AND PROVIDE A CORRECTION. MAKE SURE YOU ONLY RETURN THE CORRECTION IN VERY SHORT AND DESCRIPTIVE WAY. DONT OVERLOAD YOUR MESSAGE WITH TOO MUCH CONTENT. BE ON POINT. PROVIDE THE BEST SOLUTION.
        ERROR MESSAGE (ADD "ERROR IS: [ERROR MESSAGE]" AND THEN "FIX BY AI:" IN YOUR RESPONSE)):
        {error_msg}
        THE CODE IN WHICH THE ERROR IS SHOWING UP: (LEAVE THIS IF IT IS EMPTY)
        PROVIDE THE FIXED PART OF THE CODE IN THE END BY ADDING "FIXED CODE:" IN YOUR RESPONSE AND FIX THE LINE/LINES CAUSING THE ISSUE. 
        {code_context}
        '''
        response = model.generate_content(prompt)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
