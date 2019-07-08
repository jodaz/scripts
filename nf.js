const limit = process.argv[3];
const datePrompt = process.argv[2];
let totalDays = 0;
let passDays = 0;
let isMonthly = false;
const options  = {weekday: 'short', year: 'numeric', month: 'long', day: 'numeric'};

Date.prototype.addDays = function(days) {
    var date = new Date(datePrompt);
    date.setDate(date.getDate() + days);
    return date.toLocaleDateString('en-US', options);
}

var date = new Date();


while (passDays <= limit) {
    totalDays += passDays;

    console.log("Reboot on " + date.addDays(totalDays) + ". Days since last reboot: " + passDays);

    if (passDays % 10 == 0 && passDays != 0) {
        passDays += passDays / 5;
    } else {
        passDays += 1;
    }
}

console.log("Total days since start of recovery: %s", (totalDays));