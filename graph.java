/**
 * Author: YU LU
 * In computer science, a topological sort or topological ordering of a directed * graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constrains that one task mush be performed before another. In this application, a topological ordering is just a valid sequence for the tasks. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any DAG in linear time.
 */

import java.util.LinkedList;

class Graph
{
	protected int[] graph[] = {
		{0,1,1,0,0,0,0},
		{0,0,0,1,0,0,0},
		{0,0,0,0,1,0,0},
		{0,0,0,0,1,0,0},
		{0,0,0,0,0,0,1},
		{0,0,0,0,0,0,1},
		{0,0,0,0,0,0,0}
	};
 	
	protected LinkedList<Integer> list = new LinkedList<Integer>();
	protected LinkedList<Integer>  ts = new LinkedList<Integer>();
	protected int len;

	public void construct()
	{
		len = graph.length;
		System.out.println(len);
		
		//put notes are not pointed to in the list
		int sum = 0;
		for(int i = 0; i < len; i++){
			for(int j = 0; j < len; j++)
			{
				sum += graph[j][i];
			}
			
			if(sum == 0){
				System.out.print("start note: ");
				System.out.println(i);
				list.add(i);
			}
			sum = 0;
		}
			
	}

	public void topologicalSort()
	{
		while(list.size() != 0){
			//	System.out.print("size of list: ");
			//  System.out.println(list.size());

			int t = list.pollFirst();
			ts.add(t);

			for(int i = 0; i < len; i++)
			{
				int value = graph[t][i];
				if(value == 1){
					graph[t][i] = 0;

					int sum = 0;
					for(int j = 0; j < len; j++)
						sum += graph[j][i];

					if(sum == 0)
						list.add(i);
				}
			}
		}
		
		System.out.println(ts);
	}
}

class GraphTopoTest
{
	public static void main(String[] args)
	{
		Graph g = new Graph();
		g.construct();
		g.topologicalSort();
	}
}
