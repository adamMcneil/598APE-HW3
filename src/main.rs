use std::time::Instant;
#[derive(Clone, Copy)]
struct Planet {
    mass: f64,
    x: f64,
    y: f64,
    vx: f64,
    vy: f64,
}

struct Rng {
    seed: u64,
}

impl Rng {
    fn new() -> Self {
        Rng { seed: 100 }
    }

    fn next_u64(&mut self) -> u64 {
        self.seed ^= self.seed << 21;
        self.seed ^= self.seed >> 35;
        self.seed ^= self.seed << 4;
        self.seed
    }

    fn next_f64(&mut self) -> f64 {
        let next = self.next_u64() >> (64 - 26);
        let next2 = self.next_u64() >> (64 - 26);
        ((next << 27) + next2) as f64 / (1i64 << 53) as f64
    }
}

fn simulate_step(planets: &mut Vec<Planet>, dt: f64) {
    let n = planets.len();
    for i in 0..n {
        for j in (i + 1)..n {
            let dx = planets[j].x - planets[i].x;
            let dy = planets[j].y - planets[i].y;
            let dist_sqr = dx * dx + dy * dy + 0.0001;
            let inv_dist = (planets[i].mass * planets[j].mass) / dist_sqr.sqrt();
            let inv_dist3 = inv_dist * inv_dist * inv_dist;

            let xc = dt * dx * inv_dist3;
            let yc = dt * dy * inv_dist3;

            planets[i].vx += xc;
            planets[i].vy += yc;

            planets[j].vx -= xc;
            planets[j].vy -= yc;
        }
        planets[i].x += dt * planets[i].vx;
        planets[i].y += dt * planets[i].vy;
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: {} <nplanets> <timesteps>", args[0]);
        std::process::exit(1);
    }

    let nplanets: usize = args[1].parse().unwrap_or(100);
    let timesteps: usize = args[2].parse().unwrap_or(1000);
    let dt = 0.001;
    let mut rng = Rng::new();

    // Initialize planets
    let mut planets: Vec<Planet> = Vec::with_capacity(nplanets);
    for _ in 0..nplanets {
        let mass = rng.next_f64() * 10.0 + 0.2;
        let scale = 100.0 * (1.0 + nplanets as f64).powf(0.4);
        planets.push(Planet {
            mass,
            x: (rng.next_f64() - 0.5) * scale,
            y: (rng.next_f64() - 0.5) * scale,
            vx: rng.next_f64() * 5.0 - 2.5,
            vy: rng.next_f64() * 5.0 - 2.5,
        });
    }

    let start_time = Instant::now();
    for _ in 0..timesteps {
        simulate_step(&mut planets, dt);
    }
    let duration = start_time.elapsed();

    println!(
        "Total time to run simulation: {:.6} seconds\nFinal position: x={:.6} y={:.6}",
        duration.as_secs_f64(),
        planets.last().unwrap().x,
        planets.last().unwrap().y
    );
}
