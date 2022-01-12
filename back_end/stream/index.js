const express = require("express");
const app = express();
const fs = require("fs");

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.get("/video/:movieName", function (req, res) {
  // Ensure there is a range given for the video
  const range = req.headers.range;
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  const videoPath = `${req.params.movieName}.mp4`;
  const videoSize = fs.statSync(`${req.params.movieName}.mp4`).size;

  // Parse Range
  // Example: "bytes=32324-"
  const CHUNK_SIZE = 10 ** 6; // 1MB
  const start = Number(range.replace(/\D/g, ""));
  const end = Math.min(start + CHUNK_SIZE, videoSize - 1);

  // Create headers
  const contentLength = end - start + 1;
  const headers = {
    "Content-Range": `bytes ${start}-${end}/${videoSize}`,
    "Accept-Ranges": "bytes",
    "Content-Length": contentLength,
    "Content-Type": "video/mp4",
  };

  // HTTP Status 206 for Partial Content
  res.writeHead(206, headers);

  // create video read stream for this particular chunk
  const videoStream = fs.createReadStream(videoPath, { start, end });

  // Stream the video chunk to the client
  videoStream.pipe(res);
});

app.listen(5500, function () {
  console.log("Listening on port 5500!");
});

// const express = require("express");
// const fs = require("fs");
// const path = require("path");
// const app = express();

// app.use(express.static(path.join(__dirname, "public")));

// app.get("/", function (req, res) {
//   res.sendFile(path.join(__dirname + "/index.htm"));
// });

// app.get("/video", function (req, res) {
//   const path = "assets/sample.mp4";
//   const stat = fs.statSync(path);
//   const fileSize = stat.size;
//   const range = req.headers.range;

//   if (range) {
//     const parts = range.replace(/bytes=/, "").split("-");
//     const start = parseInt(parts[0], 10);
//     const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

//     if (start >= fileSize) {
//       res
//         .status(416)
//         .send("Requested range not satisfiable\n" + start + " >= " + fileSize);
//       return;
//     }

//     const chunksize = end - start + 1;
//     const file = fs.createReadStream(path, { start, end });
//     const head = {
//       "Content-Range": `bytes ${start}-${end}/${fileSize}`,
//       "Accept-Ranges": "bytes",
//       "Content-Length": chunksize,
//       "Content-Type": "video/mp4",
//     };

//     res.writeHead(206, head);
//     file.pipe(res);
//   } else {
//     const head = {
//       "Content-Length": fileSize,
//       "Content-Type": "video/mp4",
//     };
//     res.writeHead(200, head);
//     fs.createReadStream(path).pipe(res);
//   }
// });

// app.listen(3000, function () {
//   console.log("Listening on port 3000!");
// });
