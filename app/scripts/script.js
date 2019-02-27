angular.module('app', []).controller('ctrl', function ($scope) {
	$scope.searchText = "Type here";
	$scope.searchChanged = function () {
		// console.log('changed', $scope.seach);
	}
}).directive('contenteditable', function () {
	return {
		require: 'ngModel',
		restrict: 'A',
		link: function (scope, elm, attr, ngModel) {

			function removeChild(shouldAdd) {
				let text = "";
				let childNode = this.getElementsByTagName("span")[0];
				if (shouldAdd) {
					text += childNode.innerText;
				}
				this.removeChild(childNode);
				return text;
			}

			function updateEditableValue(text) {
				this.innerText = this.innerText + text;
				setCaret.call(this);
			}

			var items = ["Hello", "World", "Please", "Work", "Augmedix", "Make", "Believe"];
			function getWord() {
				var item = items[Math.floor(Math.random() * items.length)];
				return item;
			}

			function updateViewValue(evt) {
				if (evt.keyCode == 37 && scope.dynamic_word_added) {
					removeChild.call(this, false);
					scope.dynamic_word_added = false;
				}
				else if (evt.keyCode == 39 && scope.dynamic_word_added) {
					let text = removeChild.call(this, true);
					updateEditableValue.call(this, text);
					ngModel.$setViewValue(this.innerText);
					scope.dynamic_word_added = false;
				}
				else if (evt.keyCode == 32) {
					pasteHtmlAtCaret(`<span style="color:white;">${getWord()}&nbsp;</span>`, false);
					scope.dynamic_word_added = true;
				} else {
					if (scope.dynamic_word_added) {
						let text = removeChild.call(this, true);
						updateEditableValue.call(this, text);
						scope.dynamic_word_added = false;
					}
					ngModel.$setViewValue(this.innerText);
				}
			}

			//Or bind it to any other events
			elm.on('keyup', updateViewValue);

			scope.$on('$destroy', function () {
				elm.off('keyup', updateViewValue);
			});

			ngModel.$render = function () {
				elm.html(ngModel.$viewValue);
			}

			function setCaret() {
				// var el = document.getElementById("test");
				var el = this;
				var range = document.createRange();
				var sel = window.getSelection();
				range.setStart(el.childNodes[el.childNodes.length - 1], el.childNodes[el.childNodes.length - 1].length);
				range.collapse(true);
				sel.removeAllRanges();
				sel.addRange(range);
				el.focus();
			}

			function pasteHtmlAtCaret(html, selectPastedContent) {
				var sel, range;
				if (window.getSelection) {
					sel = window.getSelection();
					if (sel.getRangeAt && sel.rangeCount) {
						range = sel.getRangeAt(0);
						range.deleteContents();
						var el = document.createElement("div");
						el.innerHTML = html;
						var frag = document.createDocumentFragment(), node, lastNode;
						while ((node = el.firstChild)) {
							lastNode = frag.appendChild(node);
						}
						var firstNode = frag.firstChild;
						range.insertNode(frag);

						if (lastNode) {
							range = range.cloneRange();
							range.setStartAfter(lastNode);
							if (selectPastedContent) {
								range.setStartBefore(firstNode);
							} else {
								range.collapse(true);
							}
							sel.removeAllRanges();
							sel.addRange(range);
						}
					}
				} else if ((sel = document.selection) && sel.type != "Control") {
					var originalRange = sel.createRange();
					originalRange.collapse(true);
					sel.createRange().pasteHTML(html);
					var range = sel.createRange();
					range.setEndPoint("StartToStart", originalRange);
					range.select();
				}
			}

		}
	}
});

