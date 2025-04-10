#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>

float tdiff(struct timeval *start, struct timeval *end) {
  return (end->tv_sec - start->tv_sec) + 1e-6 * (end->tv_usec - start->tv_usec);
}

struct Planet {
  double mass;
  double x;
  double y;
  double vx;
  double vy;
};

unsigned long long seed = 100;

unsigned long long randomU64() {
  seed ^= (seed << 21);
  seed ^= (seed >> 35);
  seed ^= (seed << 4);
  return seed;
}

double randomDouble() {
  unsigned long long next = randomU64();
  next >>= (64 - 26);
  unsigned long long next2 = randomU64();
  next2 >>= (64 - 26);
  return ((next << 27) + next2) / (double)(1LL << 53);
}

int nplanets;
int timesteps;
double dt;
double G;

void next(Planet *planets) {
  for (int i = 0; i < nplanets; i++) {
    for (int j = i + 1; j < nplanets; j++) {
      double dx = planets[j].x - planets[i].x;
      double dy = planets[j].y - planets[i].y;
      double distSqr = dx * dx + dy * dy + 0.0001;
      double invDist = planets[i].mass * planets[j].mass / sqrt(distSqr);
      double invDist3 = invDist * invDist * invDist;

      double xc = dt * dx * invDist3;
      double yc = dt * dy * invDist3;

      planets[i].vx = planets[i].vx + xc;
      planets[i].vy = planets[i].vy + yc;

      planets[j].vx = planets[j].vx - xc;
      planets[j].vy = planets[j].vy - yc;
    }
  }

  for (int i = 0; i < nplanets; i++) {
    planets[i].x = planets[i].x + dt * planets[i].vx;
    planets[i].y = planets[i].y + dt * planets[i].vy;
  }
}

int main(int argc, const char **argv) {
  if (argc < 2) {
    printf("Usage: %s <nplanets> <timesteps>\n", argv[0]);
    return 1;
  }
  nplanets = atoi(argv[1]);
  timesteps = atoi(argv[2]);
  dt = 0.001;
  G = 6.6743;

  Planet *planets = (Planet *)malloc(sizeof(Planet) * nplanets);
  for (int i = 0; i < nplanets; i++) {
    planets[i].mass = randomDouble() * 10 + 0.2;
    planets[i].x = (randomDouble() - 0.5) * 100 * pow(1 + nplanets, 0.4);
    planets[i].y = (randomDouble() - 0.5) * 100 * pow(1 + nplanets, 0.4);
    planets[i].vx = randomDouble() * 5 - 2.5;
    planets[i].vy = randomDouble() * 5 - 2.5;
  }

  struct timeval start, end;
  gettimeofday(&start, NULL);
  for (int i = 0; i < timesteps; i++) {
    next(planets);
    // printf("x=%f y=%f vx=%f vy=%f\n", planets[nplanets-1].x,
    // planets[nplanets-1].y, planets[nplanets-1].vx, planets[nplanets-1].vy);
  }
  gettimeofday(&end, NULL);
  printf("Total time to run simulation %0.6f seconds, final location %f %f\n",
         tdiff(&start, &end), planets[nplanets - 1].x, planets[nplanets - 1].y);

  return 0;
}
