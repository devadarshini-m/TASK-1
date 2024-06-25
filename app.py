using System;
using System.Collections.Generic;

namespace SmartGridEnergyManagementSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Smart Grid Energy Management System");

            EnergyManager energyManager = new EnergyManager();
            energyManager.Run();
        }
    }

    public class EnergyManager
    {
        private List<Device> devices;
        private EnergyMonitor energyMonitor;

        public EnergyManager()
        {
            devices = new List<Device>();
            energyMonitor = new EnergyMonitor(devices);
            InitializeDevices();
        }

        private void InitializeDevices()
        {
            devices.Add(new Device("Refrigerator", 150));
            devices.Add(new Device("Air Conditioner", 2000));
            devices.Add(new Device("Washing Machine", 500));
            devices.Add(new Device("Heater", 1500));
            devices.Add(new Device("Lights", 100));
        }

        public void Run()
        {
            bool running = true;

            while (running)
            {
                Console.Clear();
                Console.WriteLine("1. View Energy Usage");
                Console.WriteLine("2. Control Devices");
                Console.WriteLine("3. Optimize Energy Usage");
                Console.WriteLine("4. Exit");
                Console.Write("Select an option: ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        ViewEnergyUsage();
                        break;
                    case "2":
                        ControlDevices();
                        break;
                    case "3":
                        OptimizeEnergyUsage();
                        break;
                    case "4":
                        running = false;
                        break;
                    default:
                        Console.WriteLine("Invalid option. Please try again.");
                        break;
                }

                if (running)
                {
                    Console.WriteLine("\nPress Enter to continue...");
                    Console.ReadLine();
                }
            }
        }

        private void ViewEnergyUsage()
        {
            Console.Clear();
            Console.WriteLine("Energy Usage:");
            energyMonitor.DisplayEnergyUsage();
        }

        private void ControlDevices()
        {
            Console.Clear();
            Console.WriteLine("Control Devices:");
            for (int i = 0; i < devices.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {devices[i].Name} ({(devices[i].IsOn ? "On" : "Off")})");
            }
            Console.Write("Select a device to toggle: ");
            if (int.TryParse(Console.ReadLine(), out int deviceIndex) && deviceIndex > 0 && deviceIndex <= devices.Count)
            {
                devices[deviceIndex - 1].Toggle();
                Console.WriteLine($"{devices[deviceIndex - 1].Name} is now {(devices[deviceIndex - 1].IsOn ? "On" : "Off")}");
            }
            else
            {
                Console.WriteLine("Invalid device selection.");
            }
        }

        private void OptimizeEnergyUsage()
        {
            Console.Clear();
            Console.WriteLine("Optimizing Energy Usage...");
            energyMonitor.OptimizeUsage();
        }
    }

    public class EnergyMonitor
    {
        private List<Device> devices;

        public EnergyMonitor(List<Device> devices)
        {
            this.devices = devices;
        }

        public void DisplayEnergyUsage()
        {
            int totalUsage = 0;
            foreach (var device in devices)
            {
                int usage = device.IsOn ? device.PowerUsage : 0;
                totalUsage += usage;
                Console.WriteLine($"{device.Name}: {usage}W");
            }
            Console.WriteLine($"Total Energy Usage: {totalUsage}W");
        }

        public void OptimizeUsage()
        {
            // Simple optimization: Turn off devices with the highest power usage first
            devices.Sort((d1, d2) => d2.PowerUsage.CompareTo(d1.PowerUsage));

            foreach (var device in devices)
            {
                if (device.IsOn)
                {
                    device.Toggle();
                    Console.WriteLine($"{device.Name} turned off to save energy.");
                }
            }
        }
    }

    public class Device
    {
        public string Name { get; }
        public int PowerUsage { get; }
        public bool IsOn { get; private set; }

        public Device(string name, int powerUsage)
        {
            Name = name;
            PowerUsage = powerUsage;
            IsOn = false;
        }

        public void Toggle()
        {
            IsOn = !IsOn;
        }
    }
}
