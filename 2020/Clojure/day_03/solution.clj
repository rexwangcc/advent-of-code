(ns day_03.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "03")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(parse [s]
            (str/split s #""))]
    (->> file
         slurp
         str/split-lines
         (map parse))))

(defn count-trees
  "Count trees with round-robin."
  [inputs]
  (let [ncol (count (first inputs))
        nrow (count inputs)
        inputs (vec inputs)]
    (loop [col 0
           row 0
           num-trees 0]
      (if (< row nrow)
        (recur (+ col 3)
               (inc row)
               (if (= "#"
                      ;; round-robin happens here
                      (get-in inputs [row (rem col ncol)]))
                 (inc num-trees)
                 num-trees))
        num-trees))))

(defn count-trees-with-custom-slope
  "Count trees with round-robin with custom slope params."
  [inputs right down]
  (let [ncol (count (first inputs))
        nrow (count inputs)
        inputs (vec inputs)]
    (loop [col 0
           row 0
           num-trees 0]
      (if (< row nrow)
        (recur (+ col right)
               (+ row down)
               (if (= "#"
                      ;; round-robin happens here
                      (get-in inputs [row (rem col ncol)]))
                 (inc num-trees)
                 num-trees))
        num-trees))))

(defn part1
  [_]
  (let [inputs (get-lines "day_03/inputs.txt")]
    (count-trees inputs)))

(defn part2
  [_]
  (let [inputs (get-lines "day_03/inputs.txt")
        f (partial count-trees-with-custom-slope inputs)]
    (->> (map f [1 3 5 7 1] [1 1 1 1 2])
         (reduce *))))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
