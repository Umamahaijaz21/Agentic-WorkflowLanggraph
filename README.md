# Agentic-WorkflowLanggraph

The project demonstrates a task-splitting and refinement workflow through the use of a PlanAgent and a ToolAgent to solve complex user questions. It makes use of iterative refinement of tasks and feedback loops to improve reliability and efficiency. The workflow was implemented with Python with an aim of demonstrating the behavior of Langgraph to work on a process such as splitting the query into sub-tasks, solving them iteratively while reflecting on the outcomes.
**Features**
Task Splitting:
•	Breaks down a user query into individual tasks:
The PlanAgent is responsible for analyzing the user's query and breaking it down into manageable sub-tasks. This approach makes each task simpler and allows for easier processing by the ToolAgent
Task Solving:
•	Solves each sub-task using a ToolAgent that performs different operations:
After splitting the tasks, the ToolAgent comes into play to handle the execution of each sub-task. Depending on the nature of the task, the ToolAgent can perform operations like:
o	Querying external APIs (e.g., searching the web for programming frameworks)
o	Running mathematical operations (e.g., computing sums or running algorithms)
o	Interacting with other tools or libraries (e.g., using numpy to work with arrays)
Feedback Loop:
•	Uses reflection on results to refine tasks if necessary:
After each task is solved, the workflow reflects on the result to check its validity and completeness. The ToolAgent includes a reflection mechanism to determine whether the result is acceptable or requires refinement. If a problem is detected (e.g., incomplete or erroneous results), the system can provide feedback, prompting the PlanAgent to modify or refine the task list.
For example, if the result of a sub-task is empty or contains an error, the ToolAgent might return feedback like "Error: No result found" or suggest a change to the task. This feedback loop allows the system to adjust the workflow in real-time, ensuring that issues are caught early and tasks are solved efficiently.
Extensibility:
•	You can modify and extend the PlanAgent and ToolAgent to accommodate different types of tasks and tools:
The architecture is designed to be flexible and extensible. You can easily add new capabilities to the workflow by extending the functionality of the PlanAgent and ToolAgent. 
This flexibility ensures that the workflow can evolve over time to handle a broader range of tasks and use cases.

 **Workflow**
 1. PlanAgent: Responsible for splitting the main user query into smaller, manageable sub-tasks.
2. ToolAgent: Executes the sub-tasks, such as fetching data, performing calculations, or API calls.
3. Reflection and Refinement: The ToolAgent reflects on the results, providing feedback if necessary to refine or adjust the tasks for better outcomes.

 **Example Query**
The workflow handles the following query:
The query is split into two sub-tasks:
- "Search top programming languages in 2024"
- "Calculate the sum of an array"

- 
## Installation

### Prerequisites
- Python 3.x
- `numpy` library

Install numpy using pip if you don't have it:
pip install numpy


