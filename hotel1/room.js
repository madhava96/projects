
// Define an array of booked dates
const bookedDates = ['2023-03-15', '2023-03-20', '2023-03-25'];

// Define a function to check if a date is already booked
function isBooked(date) {
  return bookedDates.includes(date);
}

// Define a function to check if a room is available for a given date range
function isRoomAvailable(startDate, endDate) {
  // Convert start and end dates to milliseconds
  const startMs = new Date(startDate).getTime();
  const endMs = new Date(endDate).getTime();

  // Iterate over the date range and check if any dates are already booked
  for (let currentMs = startMs; currentMs <= endMs; currentMs += 86400000) {
    const currentDate = new Date(currentMs).toISOString().slice(0, 10);
    if (isBooked(currentDate)) {
      return false;
    }
  }

  // If no dates are already booked, the room is available
  return true;
  
}