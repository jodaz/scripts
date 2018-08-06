var limit = 0;
let total_days = 0;
let isMonthly = false;

const datePrompt = process.argv[2];

Date.prototype.addDays = function(days) {
    var date = new Date(datePrompt);
    date.setDate(date.getDate() + days);
    return date;
}

var date = new Date();

while (!isMonthly) {
    total_days += limit;
    console.log("Reboot " + date.addDays(total_days) + ". Days since last reboot: " + limit);

    if (limit % 10 == 0 && limit != 0) {
        limit += 3;
    } else {
        limit += 1;
    }

    if (limit >= 30) {
        isMonthly = true;
    }
}

console.log("Total days since start of recovery: %s", (total_days));