import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class hello extends PApplet {

int rectSize = 40; 
int step = 50;

public void setup() {
  size(512, 512);
}

public void draw() {
  for (int x = 0; x < width; x += step) {
    for (int y = 0; y < height; y += step) {
      stroke(random(100));
      rect(x, y, rectSize, rectSize);
    }
  }
}

  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "hello" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
