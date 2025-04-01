import streamlit as st
from .state_graph import graph

def main(topic):
    # Inputs
    max_analysts = 3 
    thread = {"configurable": {"thread_id": "1"}}

    # Run the graph until the first interruption
    for event in graph.stream({"topic":topic,
                            "max_analysts":max_analysts}, 
                            thread, 
                            stream_mode="values"):
        
        analysts = event.get('analysts', '')
        # if analysts:
        #     for analyst in analysts:
        #         print(f"Name: {analyst.name}")
        #         print(f"Affiliation: {analyst.affiliation}")
        #         print(f"Role: {analyst.role}")
        #         print(f"Description: {analyst.description}")
        #         print("-" * 50)

    # We now update the state as if we are the human_feedback node
    graph.update_state(thread, {"human_analyst_feedback": 
                                "Add in the CEO of the startup that owns and invented the patent"}, 
                                as_node="human_feedback")

    # Check
    for event in graph.stream(None, thread, stream_mode="values"):
        analysts = event.get('analysts', '')
        # if analysts:
        #     for analyst in analysts:
        #         print(f"Name: {analyst.name}")
        #         print(f"Affiliation: {analyst.affiliation}")
        #         print(f"Role: {analyst.role}")
        #         print(f"Description: {analyst.description}")
        #         print("-" * 50)      

    # Confirm we are happy
    graph.update_state(thread, {"human_analyst_feedback": None}, as_node="human_feedback")
    
    # Continue
    for event in graph.stream(None, thread, stream_mode="updates"):
        print("--Node--")
        node_name = next(iter(event.keys()))
        print(node_name)

    final_state = graph.get_state(thread)
    report = final_state.values.get('final_report')
    st.info(report)
