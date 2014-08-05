//nqueens problem

public class NQueen{
	//start with 0, if a queen is put and effect the corresponding 
	//position, the value increase by 1
	//if a queen is removed, the value decrease by 1
	//when there is 0, means available
	int[][] chessboard; 
	int s;
	private int Dir;
	private final int TL = 0;
	private final int TR = 1;
	private final int BL = 2;
	private final int BR = 3;

	//set up the chessboard
	public NQueen(int size){
		chessboard = new int[size][size];
		s = size;
		resetBoard();
	}


	public static void main(String args[]){
		NQueen nq = new NQueen(9);

		//start from first row, first col
		for(int i = 0; i < nq.s; i++){
			nq.resetBoard();
			//System.out.println("start from row 0 and col "+i);
			nq.putAQueen(0, i);	
			nq.tryNextRow(0, i);
			System.out.println(i+1);
		}
		
	}

	public void resetBoard(){
		for(int i = 0; i < s; i++)
			for(int j = 0; j < s; j++)
				chessboard[i][j] = 0; //empty
	

	}
	public void printBoard(){
		for(int i = 0 ; i < s; i++){
			for(int j = 0 ; j < s; j++){
				System.out.print(chessboard[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}

	private boolean tryNextRow(int r, int c){
		//it is the last already
		if(r == s-1 ){
			return true;
		}

		for(int i = 0; i<s; i++){
			if(putAQueen(r+1, i)){
			//	printBoard();
				if(!tryNextRow(r+1, i))
					removeQueen(r+1, i);
				else{	
					
					return true;
				}
			}
		}

		return false;
	}
	
	//remove the queen from the board
	private void removeQueen(int r, int c){
		setChessBoard(r, c, -1);
	}

	//put a queen if possible, otherwise return false
	private boolean putAQueen(int r, int c){
		/*for(int i = 0 ; i < s; i++){
			//check r and c
			if(chessboard[r][i] > 0 ||chessboard[i][c] > 0)
				return false;
		}
		if(!checkDiagonal(r, c, TL)||!checkDiagonal(r,c,TR)||
			!checkDiagonal(r,c,BL) || !checkDiagonal(r,c,BR))
			return false;
		*/
		if(chessboard[r][c] > 0)
			return false;
		//checked the possibility, now set the unavaialbe position
		setChessBoard(r, c, 1);
		return true;
	}
	
	//set the chessboard status when putting or removing a queen
	//move -  1: putting
	//move - -1: removing
	public void setChessBoard(int r, int c, int put){
		for(int i = 0; i < s; i++){
			chessboard[r][i] += put;
			chessboard[i][c] += put;
		}

		setDiagonal(r, c, put, TL);
		setDiagonal(r, c, put, TR);
		setDiagonal(r, c, put, BL);
		setDiagonal(r, c, put, BR);

		//itself has been counted 6 times!
		chessboard[r][c] -= 5*put;
	}

	private void setDiagonal(int r, int c, int put, int d){
		int rm = 0;
		int cm = 0;
		while(checkWithinBoard(r + rm, c + cm)){
			chessboard[r+rm][c+cm] += put;
			switch(d){
			case TL:
				rm--;cm--;break;
			case TR:
				rm--;cm++;break;
			case BL:
				rm++;cm--;break;
			case BR:
				rm++;cm++;break;
			}
		}
	}
			

	private boolean checkDiagonal(int r, int c, int d){
		int rm = 0;
		int cm = 0;
		while(checkWithinBoard(r + rm, c + cm)){
			if(chessboard[r+rm][c+cm] > 0)
				return false;

			switch(d){
			case TL:
				rm--;cm--;break;
			case TR:
				rm--;cm++;break;
			case BL:
				rm++;cm--;break;
			case BR:
				rm++;cm++;break;
			}
		}
			
		return true;
	}
	private boolean checkWithinBoard(int r, int c){
		if(r < 0 || r >= s || c < 0 || c >= s)
			return false;
		else
			return true;
	}
}
