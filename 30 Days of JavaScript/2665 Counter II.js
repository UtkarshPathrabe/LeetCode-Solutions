/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
const createCounter = function(init) {
    const initValue = init;
    let count = initValue;
    const increment = () => {
        count += 1;
        return count;
    };
    const decrement = () => {
        count -= 1;
        return count;
    };
    const reset = () => {
        count = initValue;
        return count;
    };
    return {
        increment: increment,
        decrement: decrement,
        reset: reset,
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */