int rectSize = 40; 
int step = 50;

void setup() {
  size(512, 512);
}

void draw() {
  for (int x = 0; x < width; x += step) {
    for (int y = 0; y < height; y += step) {
      stroke(random(100));
      rect(x, y, rectSize, rectSize);
    }
  }
}

