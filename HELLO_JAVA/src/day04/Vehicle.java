package day04;

public class Vehicle {
	int wheelCount = 2;
	
	public void flex() {
		wheelCount = 4;
	}
	
	public static void main(String[] args) {
		Vehicle v = new Vehicle();
		System.out.println(v.wheelCount);
		v.flex();
		System.out.println(v.wheelCount);
	}
}
