/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
var daysBetweenDates = function(date1, date2) {
    const firstDate = new Date(date1)
    const secondDate = new Date(date2)
    let difference = Math.abs(firstDate - secondDate) / (1000 * 60 * 60 * 24)
    return difference
};
