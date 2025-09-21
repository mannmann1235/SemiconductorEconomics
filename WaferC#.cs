using System;
using System.Diagnostics;
using System.Threading;

class Program
{
    static void Main(string[] args)
    {
        // Creates a new Stopwatch instance to measure CPU usage.
        var cpuCounter = new PerformanceCounter("Processor", "% Processor Time", "_Total");
        
        // Creates a new PerformanceCounter instance to measure Memory.
        var ramCounter = new PerformanceCounter("Memory", "Available MBytes");

        Console.WriteLine("Measuring CPU and Memory Usage...");
        Console.WriteLine("Press Ctrl+C to stop.");

        while (true)
        {
            // Runs the PerformanceCounter.
            cpuCounter.NextValue();
            Thread.Sleep(1000); // Waits 1 second for a correct reading.

            // Gets the current CPU and Memory values.
            float currentCpuUsage = cpuCounter.NextValue();
            float currentRamAvailable = ramCounter.NextValue();

            // Displays the result on the console.
            Console.Clear(); // Clears the console for a new result.
            Console.WriteLine($"Current CPU Usage: {currentCpuUsage:F2}%");
            Console.WriteLine($"Available Memory: {currentRamAvailable:F2} MB");

            Thread.Sleep(2000); // Waits 2 seconds before updating.
        }
    }
}