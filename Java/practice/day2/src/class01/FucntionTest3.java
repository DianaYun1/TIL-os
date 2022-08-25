package class01;

public class FucntionTest3 {
	public static void main(String[] args) {
		System.out.println("아침에 일어난다");
		edu();
		move("집", "대중교통");
		
		
	}
	public static void edu() {
		System.out.println("오전 수업");
		System.out.println("점심시간");
		System.out.println("오후 수업");
		
	}
	public static void move(String place, String by) {
		System.out.println(place +"(으)로 " + by +"(을)를 이용해 이동한다.");
	}
}

