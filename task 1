<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Home Automation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e9ecef;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 900px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .section {
            margin-bottom: 30px;
        }
        .section h2 {
            margin-top: 0;
            color: #007bff;
        }
        .control-group {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        .control-group label {
            flex: 1;
            font-size: 1.1em;
            color: #555;
        }
        .control-group select, .control-group input {
            flex: 2;
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .button {
            display: block;
            width: 100%;
            padding: 15px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            text-align: center;
            margin-top: 10px;
        }
        .button:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Smart Home Automation System</h1>

        <!-- Lighting Control Section -->
        <div class="section">
            <h2>Lighting Control</h2>
            <div class="control-group">
                <label for="living-room-light">Living Room:</label>
                <select id="living-room-light">
                    <option value="off">Off</option>
                    <option value="dim">Dim</option>
                    <option value="on">On</option>
                </select>
            </div>
            <div class="control-group">
                <label for="bedroom-light">Bedroom:</label>
                <select id="bedroom-light">
                    <option value="off">Off</option>
                    <option value="dim">Dim</option>
                    <option value="on">On</option>
                </select>
            </div>
            <div class="control-group">
                <label for="kitchen-light">Kitchen:</label>
                <select id="kitchen-light">
                    <option value="off">Off</option>
                    <option value="dim">Dim</option>
                    <option value="on">On</option>
                </select>
            </div>
            <button class="button" onclick="updateLights()">Update Lights</button>
        </div>

        <!-- Climate Control Section -->
        <div class="section">
            <h2>Climate Control</h2>
            <div class="control-group">
                <label for="climate-mode">Mode:</label>
                <select id="climate-mode">
                    <option value="cool">Cool</option>
                    <option value="heat">Heat</option>
                    <option value="fan">Fan</option>
                </select>
            </div>
            <div class="control-group">
                <label for="temperature">Set Temperature:</label>
                <input type="number" id="temperature" min="60" max="80" value="70">
            </div>
            <button class="button" onclick="updateClimate()">Set Climate</button>
        </div>

        <!-- Security System Section -->
        <div class="section">
            <h2>Security System</h2>
            <div class="control-group">
                <label for="security-system">System Status:</label>
                <select id="security-system">
                    <option value="armed">Armed</option>
                    <option value="disarmed">Disarmed</option>
                </select>
            </div>
            <div class="control-group">
                <label for="door-lock">Front Door Lock:</label>
                <select id="door-lock">
                    <option value="locked">Locked</option>
                    <option value="unlocked">Unlocked</option>
                </select>
            </div>
            <button class="button" onclick="updateSecurity()">Update Security</button>
        </div>
    </div>

    <script>
        function updateLights() {
            var livingRoomLight = document.getElementById('living-room-light').value;
            var bedroomLight = document.getElementById('bedroom-light').value;
            var kitchenLight = document.getElementById('kitchen-light').value;
            alert('Lights Updated:\nLiving Room: ' + livingRoomLight + '\nBedroom: ' + bedroomLight + '\nKitchen: ' + kitchenLight);
        }

        function updateClimate() {
            var mode = document.getElementById('climate-mode').value;
            var temperature = document.getElementById('temperature').value;
            alert('Climate Set to:\nMode: ' + mode + '\nTemperature: ' + temperature + '°F');
        }

        function updateSecurity() {
            var securityStatus = document.getElementById('security-system').value;
            var doorLock = document.getElementById('door-lock').value;
            alert('Security Updated:\nSystem: ' + securityStatus + '\nFront Door: ' + doorLock);
        }
    </script>
</body>
</html>
