const std = @import("std");
const math = std.math;
const time = std.time;

const Planet = struct {
    mass: f64,
    x: f64,
    y: f64,
    vx: f64,
    vy: f64,
};

const SimulationConfig = struct {
    nplanets: usize,
    timesteps: usize,
    dt: f64 = 0.001,
    G: f64 = 6.6743e-11,
    seed: u64 = 100,
};

fn simulateStep(
    planets: []Planet,
    dt: f64,
    G: f64,
    allocator: std.mem.Allocator,
) ![]Planet {
    var new_planets = try allocator.dupe(Planet, planets);
    defer allocator.free(planets);

    // Calculate velocity changes
    for (0..planets.len) |i| {
        for (i + 1..planets.len) |j| {
            const dx = planets[j].x - planets[i].x;
            const dy = planets[j].y - planets[i].y;
            const dist_sqr = dx * dx + dy * dy + 0.0001;
            const inv_dist = G * planets[i].mass * planets[j].mass / math.sqrt(dist_sqr);
            const inv_dist3 = inv_dist / dist_sqr;

            new_planets[i].vx += dt * dx * inv_dist3;
            new_planets[i].vy += dt * dy * inv_dist3;

            new_planets[j].vx -= dt * dx * inv_dist3;
            new_planets[j].vy -= dt * dy * inv_dist3;
        }
    }

    // Update positions
    for (new_planets) |*planet| {
        planet.x += dt * planet.vx;
        planet.y += dt * planet.vy;
    }

    return new_planets;
}

fn initPlanets(config: SimulationConfig, allocator: std.mem.Allocator) ![]Planet {
    var planets = try allocator.alloc(Planet, config.nplanets);
    var prng = std.rand.DefaultPrng.init(config.seed);
    const rng = prng.random();

    for (planets) |*planet| {
        const scale = 100.0 * math.pow(f64, @as(f64, @floatFromInt(config.nplanets)) + 1, 0.4);
        planet.* = .{
            .mass = rng.float(f64) * 10.0 + 0.2,
            .x = (rng.float(f64) - 0.5) * scale,
            .y = (rng.float(f64) - 0.5) * scale,
            .vx = rng.float(f64) * 5.0 - 2.5,
            .vy = rng.float(f64) * 5.0 - 2.5,
        };
    }

    return planets;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
}


