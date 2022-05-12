const express =require('express');
const expressLayouts=require('express-ejs-layouts');
const flash=require('connect-flash');
const session=require('express-session');
const bodyParser=require('body-parser');
const mongoose=require('mongoose');
const passport=require('passport');
const app=express();
const PORT=process.env.PORT||5000;

require('./config/passport')(passport);

// DB config

const connect=mongoose.connect('mongodb://localhost:27017/nodeApp', {useNewUrlParser: true, useCreateIndex:true,useUnifiedTopology: true });

connect.then((db) => {
  console.log("Connected to DataBase nodeApp");
}, (err) => { console.log(err); });



// commands to run "npm run dev" or "npm start"....prefer "npm run dev"
app.listen(PORT,()=>{
    console.log(`Connected to localhost:${PORT}`);

});

// BODY PARSER
app.use(express.urlencoded({extended:false}));

// EXPRESS SESSION

app.use(session({
  secret:'secret',
  resave:true,
  saveUninitialized:true,

}));

// Passport middleware
app.use(passport.initialize());
app.use(passport.session());

// Connect Flash
app.use(flash());

// Global variables
app.use(function(req, res, next) {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  next();
});
// EJS
app.use(expressLayouts);
app.set('view engine','ejs');


// ROUTES
const indexRouter=require('./routes/index.js');
const userRouter=require('./routes/users.js');
app.use('/',indexRouter);
app.use('/users',userRouter);
