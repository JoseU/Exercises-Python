int rectSize = 40; 

void setup() {
  size(512, 512);
}

void draw() {
  for (int x = 0; x < width; ++x) {
    for (int y = 0; y < height; ++y) {
      stroke(random(100));
      rect(x, y, rectSize, rectSize);
    }
  }
}