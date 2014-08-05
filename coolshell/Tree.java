
public class Tree{
	static class TreeNode {
		char val;
		TreeNode left;
		TreeNode right;
		TreeNode(char x){ val = x;}
	}
	private static TreeNode tree;

	public static TreeNode buildTree(char[] inorder, char[] postorder){
		int inStart = 0;
		int inEnd = inorder.length - 1;
		int postStart = 0;
		int postEnd = postorder.length - 1;

		return buildTree(inorder, inStart, inEnd, postorder, postStart, postEnd);
	}

	public static TreeNode buildTree(char[] inorder, int inStart, int inEnd,
				char[] postorder, int postStart, int postEnd){
		if(inStart > inEnd || postStart > postEnd)
			return null;
		char rootValue = postorder[postEnd];
		TreeNode root = new TreeNode(rootValue);

		int k = 0;
		for(int i = 0; i < inorder.length; i++){
			if(inorder[i] == rootValue){
				k = i;
				break;
			}
		}

		root.left = buildTree(inorder, inStart, k-1, postorder, postStart, postStart+k-(inStart+1));
		root.right = buildTree(inorder, k+1, inEnd, postorder, postStart + k - inStart, postEnd-1);

		return root;
	}

	public static void FindPath(TreeNode root){
		while(root != null){
			System.out.println(" " +root.val);

			int lh = height(root.left);
			int rh = height(root.right);

			if (lh > rh){
				root = root.left;
			}else{
				root = root.right;
			}
		}		
			
	}

	public static int height(TreeNode root){
		if(root == null)
			return 0;

		return 1+max(height(root.left), height(root.right));
	}

	public static int max(int a, int b){
		return a >= b ? a:b;
	}

	

	public static void main(String agrs[]){
		String in = "T, b, H, V, h, 3, o, g, P, W, F, L, u, A, f, G, r, m, 1, x, J, 7, w, e, 0, i, Q, Y, n, Z, 8, K, v, q, k, 9, y, 5, C, N, B, D, 2, 4, U, l, c, p, I, E, M, a, j, 6, S, R, O, X, s, d, z, t";
		String po = "T, V, H, o, 3, h, P, g, b, F, f, A, u, m, r, 7, J, x, e, w, 1, Y, Q, i, 0, Z, n, G, L, K, y, 9, k, q, v, N, D, B, C, 5, 4, c, l, U, 2, 8, E, I, R, S, 6, j, d, s, X, O, a, M, p, W, t, z";

		in = in.replace(", ", "");
		char[] inorder = in.toCharArray();
		po = po.replace(", ", "");
		char[] postorder = po.toCharArray();
		
		tree = buildTree(inorder, postorder);
		FindPath(tree);
	}

}
