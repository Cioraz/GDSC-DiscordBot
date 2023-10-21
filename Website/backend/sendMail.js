// const nodemailer = require('nodemailer');
// require('dotenv').config()

// const sendMail = async (email) => {
//     // create reusable transporter object using the default SMTP transport
//     let smtpConfig = {
//         host: 'smtp.gmail.com',
//         port: 465,
//         secure: true, // use SSL
//         auth: {
//             user: 'gdscdiscord3@gmail.com',
//             pass: 'Sunil1029!'
//         }A
//     };
//     let transporter = nodemailer.createTransport(smtpConfig);

//     // send mail with defined transport object
//     let info = await transporter.sendMail({
//         from: '"GDSC Discord Bot" <Wec_Discord@gmail.com>', // sender address
//         to: email, // list of receivers
//         subject: "Registered Succesfully!", // Subject line
//         text: "You have been registered on the WEC database.", // plain text body
//         html: `<h1>You have Successfully Registered on WEC Database. Welcome to the group!. Here is the discord invite link https://discord.gg/XRBbmW5k`, // html body
//     });
//     console.log(info.messageId);
// }

// // Exporting the function
// module.exports = sendMail;