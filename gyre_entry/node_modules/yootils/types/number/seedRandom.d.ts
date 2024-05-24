/**
 * Create a seeded random number generator that returns a random number between `a` and `b`, or between 0 and `a` if `b` is unspecified
 * @param {string} seed
 */
export default function seedRandom(seed: string): (a: number, b?: number) => number;
