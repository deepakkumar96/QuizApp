/* widgets or objects defination */


function Time(minute, second){
	this.minute = 10 || minute;
	this.second = 0;
}

Time.prototype.getTime = function(){
	return this.minute + " : " + this.second;
}

Time.prototype.increment = function(){
	if(!this.isComplete()){
		this.second--;
		if(this.second < 0){
			this.second = 59;
			this.minute--;
		}
	}
}

Time.prototype.isComplete = function(){
	if(this.minute <= 0 & this.second <= 0)
		return true;
	else
		return false;	
}