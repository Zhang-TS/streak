import java.util.LinkedList;

class Graph
{
	/* How a multi-dimension array is defined*/
	protected int[] graph[] = {
			{0,1,1,0,0,0,0},
			{0,0,0,1,0,0,0},
			{0,0,0,0,1,0,0},
			{0,0,0,0,1,0,0},
			{0,0,0,0,0,0,1},
			{0,1,1,0,0,0,1},
			{0,0,0,0,0,0,0},
	};

	protected LinkedList<Integer> list = new LinkedList<Integer>();
	protected LinkedList<Integer> ts = new LinkedList<Integer>();
	protected int len;

	public void construct()
	{
		len = graph.length;
		
		//put vertex that are not pointed to in the list
		int sum = 0;
		for(int i = 0; i < len; i++){
			for(int j =0; j < len; j++)
			{
				sum += graph[j][i];
			}

			if(sum == 0){
				list.add(i);
			}
			sum = 0;
		}
	}

	public void topologicalSort()
	{
		while(list.size() != 0){
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

public class GraphTopoSort
{
	public static void main(String[] args)
	{
		Graph g = new Graph();
		g.construct();
		g.topologicalSort();
	}
}
