(function() {


angular
	.module('onlineResume')
	.controller('homeCtrl', homeCtrl);

homeCtrl.$inject = ['onlineResumeData']

function homeCtrl(onlineResumeData) {
	var vm = this;

	onlineResumeData.apiGetResumeJson()
		.success(function(data){
			vm.data = data['resume'];
		})
		.error(function(e){
			console.log(e);
		});


};


})();