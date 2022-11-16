function deleteFood(foodId) {
  console.log("Click")
    fetch("/delete-food", {
      method: "POST",
      body: JSON.stringify({ foodId: foodId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }