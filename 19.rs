// You are given the following information, but you may prefer to do some research for yourself.

// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

fn main() {
    let mut sunday_count = 0;
    let mut days = 1; // Offset it, six days after monday is sunday
    let months_length = [31,28,31,30,31,30,31,31,30,31,30,31];

    for year in 1900..=2000 {
        let is_leap = year%4 == 0 && (year%100 != 0|| year%400==0);

        for month in 1..=12 {

            if days%7 == 0 {
                if year > 1900 {
                    println!("Year {} on month {} has first as Sunday",year,month);
                    sunday_count+=1;
                }
            }

            if month == 2 && is_leap {
                days += 29;
            } else {
                days += months_length[month-1];
            }
            
        }
    }

    println!("{}",sunday_count) // 171
}