<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>test</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
    <script>
        window.setInterval('refresh()', 200); 	
        var t = 1;
        var temp = [41,100,-59,55,-19,-98,44,-28,63,37,-96,34,-70,37,27,-50,8,26,-25,-63,]
        // Refresh or reload page.
        function refresh() {
            var client = new XMLHttpRequest();
            client.open('GET', '../assets/info.txt');
            client.onload = function() {
                if (client.readyState === client.DONE) {
                    if (client.status === 200) {
                        document.getElementById("rain").textContent = "累計雨量: "+client.response.split("\n")[0]+" mm";
                        document.getElementById("soil").textContent = "土壤濕度: "+client.response.split("\n")[1]+" %";
                        var xValues = ["","","","","","","","","","","","","","","","","","","",""]
                        for (let i = 0; i < 20; i++) {
                            temp[i]=temp[(i+1)%20];
                        }
                        new Chart("XChart", {
                        type: "line",
                        data: {labels: xValues,datasets: [{lineTension: 0,data: temp,borderColor: "#FFAC55",fill: false}]},
                        options: {legend: {display: false},animation: {duration: 0},scales: {yAxes: [{display: true,stacked: true,ticks: {min: -100,max: 100}}]}}
                        });
                        // new Chart("XChart", {
                        // type: "line",
                        // data: {labels: xValues,datasets: [{lineTension: 0,data: client.response.split("\n")[2].split("x"),borderColor: "#FFAC55",fill: false}]},
                        // options: {legend: {display: false},animation: {duration: 0},scales: {yAxes: [{display: false,stacked: true,ticks: {min: 100,max: 250}}]}}
                        // });
                        new Chart("YChart", {
                        type: "line",
                        data: {labels: xValues,datasets: [{lineTension: 0,data: client.response.split("\n")[3].split("x"),borderColor: "#00AD44",fill: false}]},
                        options: {legend: {display: false},animation: {duration: 0},scales: {yAxes: [{display: false,stacked: true,ticks: {min: 100,max: 250}}]}}
                        });
                        new Chart("ZChart", {
                        type: "line",
                        data: {labels: xValues,datasets: [{lineTension: 0,data: client.response.split("\n")[4].split("x"),borderColor: "#5596ff",fill: false}]},
                        options: {legend: {display: false},animation: {duration: 0},scales: {yAxes: [{display: false,stacked: true,ticks: {min: 100,max: 250}}]}}
                        });
                    }
                }
            }
            client.send();

        }
     </script>
</head>

<body>
    <div style="flex-direction:column;">
        <img style="max-height:700px;width:100%;" src="../assets/main.jpg">
        <div style="text-align: center;width:100%;">
            <p style="font-size: 40px;float: left;width:50%" id="rain">累計雨量:  mm</p>
            <p style="font-size: 40px;float: left;width:50%" id="soil">土壤濕度:  %</p>
        </div>
        <hr size="5px" align="center" width="100%">
        <div style="display: flex;align-items:center;">
            <p style="text-align:center;font-size: 40px;width:25%">X軸震動: </p>
            <canvas id="XChart" style="max-width:50%;max-height:300px;border-width:3px;border-style:solid;border-color:#FFAC55;padding:5px;"></canvas>    
        </div>
        <p style="text-align:center;margin:0 auto;font-size: 40px;width:100%">時間軸</p>
        <hr size="5px" align="center" width="100%">
        <div style="display: flex;align-items:center;">
            <p style="text-align:center;font-size: 40px;width:25%">Y軸震動: </p>
            <canvas id="YChart" style="max-width:50%;max-height:300px;border-width:3px;border-style:solid;border-color:#00AD44;padding:5px;"></canvas>
        </div>
        <p style="text-align:center;margin:0 auto;font-size: 40px;width:100%">時間軸</p>
        <hr size="5px" align="center" width="100%">
        <div style="display: flex;align-items:center;">
            <p style="text-align:center;font-size: 40px;width:25%">Z軸震動: </p>
            <canvas id="ZChart" style="max-width:50%;max-height:300px;border-width:3px;border-style:solid;border-color:#5596ff;padding:5px;"></canvas>
        </div>
        <p style="text-align:center;margin:0 auto;font-size: 40px;width:100%">時間軸</p>
        <hr size="5px" align="center" width="100%">
        <div style="display: flex;align-items:center;">
            <p style="text-align:center;font-size: 40px;width:25%">即時影像: </p>
            <div id="player" style="width:50%;height:600px;"></div>
        </div>
    </div>
    <script>
      // 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');
    
      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
      var player;
      function onYouTubeIframeAPIReady() {
        var client = new XMLHttpRequest();
        client.open('GET', '../assets/url.txt');
        client.onload = function() {
            if (client.readyState === client.DONE) {
                if (client.status === 200) {
                    player = new YT.Player('player', {
                        // width: '100%',
                        videoId: client.response,
                        playerVars: { 'autoplay': 1, 'playsinline': 1 },
                        events: {
                        'onReady': onPlayerReady
                        }
                    });
                }
            }
        }
        client.send();
      }
    
      // 4. The API will call this function when the video player is ready.
      function onPlayerReady(event) {
         event.target.mute();
        event.target.playVideo();
      }
    </script>
    <script>
        
    </script>
</body>
</html>