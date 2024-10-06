#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess

class JupyterAPI:
    def __init__(self):
        pass

    def execute(self, code):
        # Simulate Jupyter notebook execution
        try:
            exec(code)  # This will execute Python code
            return "Code executed successfully"
        except Exception as e:
            return f"Error executing code: {str(e)}"

# Example Jupyter execution
jupyter_tool = JupyterAPI()
code = """
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
"""
result = jupyter_tool.execute(code)
print(result)


# In[2]:


class ToolAgent:
    def __init__(self):
        # Instantiate the tools
        self.tools = {
            'Google': GoogleAPI(api_key="your-google-api-key", cx="your-cx-id"),
            'Jupyter': JupyterAPI()
        }

    def solve_task(self, task):
        # Depending on the sub-task, choose the appropriate tool
        if "search" in task:
            print(f"Using Google API for task: {task}")
            return self.tools['Google'].execute(task)
        elif "compute" in task:
            print(f"Using Jupyter API for task: {task}")
            return self.tools['Jupyter'].execute(task)
        else:
            return "Task type not recognized"

    def reflect_on_result(self, result):
        # Simple reflection: check if the result is valid or needs refinement
        if "Error" in result:
            return {'needs_modification': True, 'needs_deletion': False, 'needs_addition': False}
        return {}


# In[7]:


import numpy as np


# In[8]:


# Placeholder class for PlanAgent
class PlanAgent:
    def split_task(self, user_query):
        # Splitting the user query into sub-tasks (this can be more complex in a real scenario)
        return ["Search Python AI frameworks", "Compute numpy array"]

    def refine_tasks(self, feedback):
        # Modify tasks based on feedback (placeholder)
        print("Refining tasks based on feedback...")

# Placeholder class for ToolAgent
class ToolAgent:
    def solve_task(self, task):
        # Solve each task (simplified, in a real scenario, it would use APIs or tools)
        if task == "Search Python AI frameworks":
            return ["TensorFlow", "PyTorch", "Keras"]
        elif task == "Compute numpy array":
            import numpy as np
            array = np.array([1, 2, 3])
            return array
        else:
            return "Task not recognized"

    def reflect_on_result(self, result):
        # Reflect on result to check if refinement is needed (placeholder logic)
        if isinstance(result, str):
            # If result is a string (like 'Task not recognized'), check if it is empty or an error message
            if not result or "not recognized" in result:
                return "Error: No valid result found"
        elif isinstance(result, list):
            # If it's a list, check if it's empty
            if len(result) == 0:
                return "Error: No result found"
        elif isinstance(result, np.ndarray):
            # If it's a numpy array, check if it has elements
            if result.size == 0:
                return "Error: Empty numpy array"
        
        return None

# LanggraphWorkflow using PlanAgent and ToolAgent
class LanggraphWorkflow:
    def __init__(self):
        self.plan_agent = PlanAgent()
        self.tool_agent = ToolAgent()

    def run(self, user_query):
        # Outer Loop: Split tasks and iterative refinement
        sub_tasks = self.plan_agent.split_task(user_query)
        for task in sub_tasks:
            print(f"Solving Task: {task}")
            
            # Inner Loop: Solve each sub-task using ToolAgent
            result = self.tool_agent.solve_task(task)
            print(f"Result: {result}")
            
            # Reflection on result
            feedback = self.tool_agent.reflect_on_result(result)
            if feedback:
                print(f"Feedback received: {feedback}")
                self.plan_agent.refine_tasks(feedback)

        print("Workflow completed")
        return "All tasks solved"

# Example Workflow Execution
workflow = LanggraphWorkflow()
user_query = "search for Python AI frameworks and compute a simple numpy array"
workflow.run(user_query)


# In[11]:


# Placeholder class for PlanAgent
class PlanAgent:
    def split_task(self, user_query):
        # Splitting the user query into sub-tasks (this can be more complex in a real scenario)
        return ["Search top programming languages in 2024", "Calculate sum of an array"]

    def refine_tasks(self, feedback):
        # Modify tasks based on feedback (placeholder)
        print("Refining tasks based on feedback...")

# Placeholder class for ToolAgent
class ToolAgent:
    def solve_task(self, task):
        # Solve each task (simplified, in a real scenario, it would use APIs or tools)
        if task == "Search top programming languages in 2024":
            return ["Python", "JavaScript", "Go", "Rust"]
        elif task == "Calculate sum of an array":
            import numpy as np
            array = np.array([25,23,44,34])
            return np.sum(array)
        else:
            return "Task not recognized"

    def reflect_on_result(self, result):
        # Reflect on result to check if refinement is needed (placeholder logic)
        if not result:
            return "Error: No result found"
        return None

# LanggraphWorkflow using PlanAgent and ToolAgent
class LanggraphWorkflow:
    def __init__(self):
        self.plan_agent = PlanAgent()
        self.tool_agent = ToolAgent()

    def run(self, user_query):
        # Outer Loop: Split tasks and iterative refinement
        sub_tasks = self.plan_agent.split_task(user_query)
        for task in sub_tasks:
            print(f"Solving Task: {task}")
            
            # Inner Loop: Solve each sub-task using ToolAgent
            result = self.tool_agent.solve_task(task)
            print(f"Result: {result}")
            
            # Reflection on result
            feedback = self.tool_agent.reflect_on_result(result)
            if feedback:
                print(f"Feedback received: {feedback}")
                self.plan_agent.refine_tasks(feedback)

        print("Workflow completed")
        return "All tasks solved"

# Example Workflow Execution with a new query
workflow = LanggraphWorkflow()
user_query = "search for top programming languages in 2024 and calculate the sum of an array"
workflow.run(user_query)


# In[ ]:




