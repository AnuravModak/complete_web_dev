const mongoose=require('mongoose');

const UserSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true,
        default:" "
    },
    email:{
        type:String,
        required:true,
        default:" "
    },
    password:{
        type:String,
        required:true,
        default:" "
    },
    date:{
        type:Date,
        default:Date.now
    }
    


});
const User=mongoose.model('User',UserSchema);
module.exports=User;
