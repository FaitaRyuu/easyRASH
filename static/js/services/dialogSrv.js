//define dialog and toast service
var app = angular.module('myApp').factory('dialogService',
	['$mdDialog', "$mdToast",
	function ($mdDialog, $mdToast) {

		// return available functions for use in controllers
		return ({
			showSimpleToast: showSimpleToast,
			showAlertDialog: showAlertDialog,
			showConfirmDialog: showConfirmDialog,
			showAdvancedDialog: showAdvancedDialog
		});

		function showSimpleToast(text){
			$mdToast.show(
				$mdToast.simple()
				.textContent(text)
				.position("bottom right" )
				.hideDelay(3000)
			);
		}

		function showAlertDialog(ev, title, text, label, ok){
			$mdDialog.show(
		      $mdDialog.alert()
		        .clickOutsideToClose(true)
		        .title(title)
		        .textContent(text)
		        .ariaLabel(label)
		        .ok(ok)
		        .targetEvent(ev)
		    );	
		}

		function showConfirmDialog(ev, ok, cancel, title, text, label, okstatus, cancelstatus){
	    	
	    	var confirm = $mdDialog.confirm()
	    			.title(title)
	    			.textContent(text)
	    			.ariaLabel(label)
	    			.targetEvent(ev)
	    			.ok(ok)
	    			.cancel(cancel);

	    	return $mdDialog.show(confirm).then(function() {
				return okstatus;
	    	}, function() {
				return cancelstatus;		
	    	});
	    }

	    function showAdvancedDialog(url){
	    	
	    }
}]);
