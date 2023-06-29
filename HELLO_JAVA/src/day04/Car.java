package day04;

public class Car extends Vehicle {
	int autopilot_level = 1;
	
	public void hit() {
		autopilot_level++;
	}
}
