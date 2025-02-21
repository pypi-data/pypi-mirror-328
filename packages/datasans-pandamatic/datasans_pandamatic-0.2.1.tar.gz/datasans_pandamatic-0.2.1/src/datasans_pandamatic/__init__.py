from typing import Dict, Any, Union
import pandas as pd
from together import Together
from IPython.display import Code, HTML

def display_code_with_copy(code: str) -> HTML:
    """Creates an HTML display with a copy button for the code."""
    html = f"""
    <div style="position: relative;">
        <button onclick="copyCode(this)" style="position: absolute; right: 0; top: 0; z-index: 1000;
                padding: 4px 8px; background: #f0f0f0; border: 1px solid #ccc; border-radius: 4px;">
            Copy Code
        </button>
        {Code(code, language='python')._repr_html_()}
    </div>
    <script>
    function copyCode(btn) {{
        const pre = btn.parentElement.querySelector('pre');
        navigator.clipboard.writeText(pre.textContent);
        btn.textContent = 'Copied!';
        setTimeout(() => btn.textContent = 'Copy Code', 2000);
    }}
    </script>
    """
    return HTML(html)

def _analyze_column(series: pd.Series) -> Dict[str, Any]:
    """Analyzes a pandas Series and returns its characteristics."""
    col_info = {
        "dtype": str(series.dtype),
        "n_unique": len(series.unique()),
        "n_missing": series.isna().sum()
    }

    try:
        if pd.api.types.is_numeric_dtype(series):
            values = pd.to_numeric(series, errors="coerce")
            col_info.update({
                "min": float(values.min()),
                "max": float(values.max()),
                "mean": float(values.mean()),
                "type": "numeric"
            })
        else:
            unique_values = series.unique().tolist()[:10]
            col_info.update({
                "unique_values": unique_values,
                "type": "categorical"
            })
    except Exception as e:
        col_info.update({
            "type": "categorical",
            "error": str(e)
        })

    return col_info

def _generate_context(df: pd.DataFrame) -> str:
    """Generates context information about the DataFrame."""
    columns_info = {col: _analyze_column(df[col]) for col in df.columns}
    
    context = (f"DataFrame Info:\n"
              f"- Rows: {len(df)}\n"
              f"- Columns: {len(df.columns)}\n\n")
    context += "Column Details:\n"
    
    for col, info in columns_info.items():
        context += f"\n{col}:\n"
        context += f"- Type: {info['type']}\n"
        context += f"- Missing: {info['n_missing']}\n"
        
        if info["type"] == "numeric":
            context += f"- Range: {info['min']} to {info['max']}\n"
            context += f"- Mean: {info['mean']}\n"
        else:
            context += f"- Sample values: {', '.join(str(v) for v in info['unique_values'])}\n"
    
    return context

def _clean_code(text: str) -> str:
    """Cleans and formats the generated code."""
    # Extract code from markdown blocks if present
    code = text.strip()
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0].strip()
    elif "```" in code:
        code = code.split("```")[1].split("```")[0].strip()

    # Add required imports
    imports = [
        "import pandas as pd",
        "import matplotlib.pyplot as plt",
        "import seaborn as sns"
    ]
    
    code_lines = code.split("\n")
    existing_imports = [line for line in code_lines if line.startswith("import")]
    needed_imports = [imp for imp in imports if imp not in existing_imports]
    
    return "\n".join(needed_imports + [""] + code_lines if needed_imports else code_lines)

def gen(df: pd.DataFrame, prompt: str) -> Union[HTML, str]:
    """
    Generates pandas code based on the DataFrame and prompt.
    
    Args:
        df: Input DataFrame
        prompt: What you want to do with the data
        
    Returns:
        Generated code with copy button
    """
    try:
        context = _generate_context(df)
        
        messages = [
            {"role": "system", "content": "You are a Python data processing expert focused on DataFrame operations with correct data types handling. Provide ONLY pure Python code without any formatting or explanations."},
            {"role": "user", "content": f"""Based on the following DataFrame information:

{context}

I want you to:
{prompt}

IMPORTANT:
0. Don't define a new df, use df.copy() if needed to preserve original data.
1. Provide ONLY simple Python code.
2. Process dataframe based on column type, numeric or categorical.
3. DON'T use customerID or other ID columns as numeric values
4. Make sure the code uses the 'df' variable.
5. Don't define a new df, use df.copy() if needed to preserve original data.
6. Use clear variable names with Indonesian context.
7. Add comments in Indonesian to explain complex operations.
8. Return processed DataFrame or relevant statistics.
9. Ensure all columns used exist in the DataFrame.
10. Add data validation steps where appropriate.
11. Print detailed explanation for each output with print syntax."""}
        ]

        client = Together()
        client.api_key = "cfe07b73d607674d54a6843629292568623d695c4741e26944b2437ba918ccce"
        
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=messages
        )
        
        code = _clean_code(response.choices[0].message.content)
        return display_code_with_copy(code)
        
    except Exception as e:
        return f"# Error generating code:\n# {str(e)}"
