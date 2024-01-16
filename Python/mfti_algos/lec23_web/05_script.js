var flag = true;
function toggle(self) {
    if (flag) {
        self.style.color = 'red';
        self.innerText = 'Red';
    } else {
        self.style.color = 'green';
        self.innerText = 'Green';
    }
    flag = !flag;
}
